from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import base64
import io
from PIL import Image
import torch
from diffusers import AutoPipelineForImage2Image
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from contextlib import asynccontextmanager
from settings_api import router as settings_router, settings

# Setup logging (based on Scope pattern)
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "streamstyle.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler = RotatingFileHandler(
    log_file,
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=5
)
file_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(file_handler)

logger = logging.getLogger(__name__)

# Global state
pipe = None
executor = ThreadPoolExecutor(max_workers=1)
processing_queue = asyncio.Queue(maxsize=2)

def load_model():
    global pipe
    logger.info("🤖 Loading Stable Diffusion Turbo...")
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    
    logger.info(f"📍 Device: {device}, Dtype: {dtype}")
    
    pipe = AutoPipelineForImage2Image.from_pretrained(
        "stabilityai/sd-turbo",
        torch_dtype=dtype,
        variant="fp16" if device == "cuda" else None
    )
    
    if device == "cuda":
        pipe = pipe.to("cuda")
        try:
            pipe.unet = torch.compile(pipe.unet, mode="reduce-overhead", fullgraph=True)
            logger.info("✅ Model compiled with torch.compile")
        except:
            logger.warning("⚠️  torch.compile not available")
    
    pipe.set_progress_bar_config(disable=True)
    logger.info("✅ Model loaded!")

def process_frame(image_data: str):
    start_time = time.time()
    
    img_bytes = base64.b64decode(image_data.split(',')[1])
    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    image = image.resize((512, 512), Image.Resampling.LANCZOS)
    
    with torch.inference_mode():
        result = pipe(
            prompt=settings.prompt,
            image=image,
            num_inference_steps=settings.num_inference_steps,
            strength=settings.strength,
            guidance_scale=settings.guidance_scale
        ).images[0]
    
    buffered = io.BytesIO()
    result.save(buffered, format="JPEG", quality=85)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    elapsed = time.time() - start_time
    logger.info(f"⚡ Frame processed in {elapsed:.2f}s")
    
    return f"data:image/jpeg;base64,{img_str}"

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Starting StreamStyle AI")
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, load_model)
    yield
    logger.info("🛑 Shutting down")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(settings_router, prefix="/api", tags=["settings"])

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info("🔌 Client connected")
    
    try:
        while True:
            data = await websocket.receive_json()
            
            if data["type"] == "prompt":
                settings.prompt = data["prompt"]
                await websocket.send_json({"type": "prompt_updated", "prompt": settings.prompt})
                logger.info(f"🎨 Prompt: {settings.prompt}")
            
            elif data["type"] == "frame":
                if processing_queue.full():
                    try:
                        processing_queue.get_nowait()
                    except:
                        pass
                
                loop = asyncio.get_event_loop()
                styled_frame = await loop.run_in_executor(
                    executor,
                    process_frame,
                    data["image"]
                )
                await websocket.send_json({"type": "styled_frame", "image": styled_frame})
    
    except WebSocketDisconnect:
        logger.info("🔌 Client disconnected")
    except Exception as e:
        logger.error(f"❌ Error: {e}")

@app.get("/")
async def root():
    device = "GPU (CUDA)" if torch.cuda.is_available() else "CPU"
    return {
        "status": "StreamStyle AI v2.0",
        "device": device,
        "model": "stabilityai/sd-turbo"
    }

@app.get("/health")
async def health():
    return {"status": "ok", "model_loaded": pipe is not None}

@app.get("/readyz")
async def readiness():
    return {"status": "ready", "model_loaded": pipe is not None}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
