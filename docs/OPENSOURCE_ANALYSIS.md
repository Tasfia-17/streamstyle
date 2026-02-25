# Architecture Analysis - Open Source Projects

## Projects Analyzed

1. **GenDJ** - Real-time AI video generation for DJs
2. **GenDJ-FE** - React/TypeScript frontend with WebRTC
3. **GenDJ-API** - Node.js API with Prisma
4. **Scope** - Professional video streaming with AI
5. **Scope Audio Transcription** - Audio processing plugin

---

## Key Patterns to Adopt

### 1. WebSocket Architecture (from GenDJ)

**Pattern**: Batched frame processing with queue management
```python
# GenDJ approach - batch frames for efficiency
class ThreadedWebsocket:
    def __init__(self, batch_size=4):
        self.batch = []
        self.batch_size = batch_size
        
    async def handler(self, websocket):
        while True:
            frame = await websocket.recv()
            self.batch.append(frame)
            
            if len(self.batch) >= self.batch_size:
                # Process batch
                batch_tensor = torch.stack(self.batch[:n])
                self.batch = self.batch[n:]  # Drop processed
```

**Benefits**:
- Prevents memory overflow
- Better GPU utilization
- Smoother processing

### 2. Settings API (from GenDJ)

**Pattern**: Separate HTTP API for settings while WebSocket handles frames
```python
# settings_api.py - FastAPI for control
@app.post("/prompt/")
async def set_prompt(request: PromptRequest):
    settings.prompt = request.prompt
    return {"status": "updated"}

@app.post("/blend/")
async def set_blend(request: BlendRequest):
    settings.blend_factor = request.blend
    return {"status": "updated"}
```

**Benefits**:
- Cleaner separation of concerns
- RESTful control interface
- Easier to test and debug

### 3. Health Check System (from GenDJ handler.py)

**Pattern**: Dedicated health endpoint for monitoring
```python
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/readyz":
            self.send_response(200)
            self.wfile.write(b"OK")
```

**Benefits**:
- Production monitoring
- Load balancer integration
- Service health tracking

### 4. Frontend Architecture (from GenDJ-FE)

**Pattern**: React + TypeScript + Tailwind + Vite
```typescript
// WarpPage.tsx structure
interface Warp {
  id: string;
  jobId: string;
  jobStatus: 'IN_PROGRESS' | 'COMPLETED' | 'FAILED';
  workerId?: string;
}

const buildWebsocketUrl = (workerId?: string) => {
  return IS_LOCAL 
    ? `ws://localhost:8765`
    : `wss://${workerId}-8765.proxy.runpod.net`;
};
```

**Benefits**:
- Type safety
- Better developer experience
- Production-ready patterns

### 5. Logging System (from Scope)

**Pattern**: Structured logging with rotation
```python
# Rotating file handler
file_handler = RotatingFileHandler(
    log_file,
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=5
)

# Different log levels for different modules
logging.getLogger("scope.server").setLevel(logging.INFO)
logging.getLogger("asyncio").setLevel(logging.WARNING)
```

**Benefits**:
- Disk space management
- Better debugging
- Production monitoring

### 6. CORS Configuration (from Scope)

**Pattern**: Proper CORS for production
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 7. Async Context Manager (from Scope)

**Pattern**: Proper startup/shutdown lifecycle
```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await load_models()
    yield
    # Shutdown
    await cleanup()

app = FastAPI(lifespan=lifespan)
```

**Benefits**:
- Clean resource management
- Proper cleanup
- No resource leaks

---

## Improvements for StreamStyle AI

### 1. Add Settings API
Create separate endpoint for controls (prompt, strength, etc.)

### 2. Implement Batching
Process multiple frames together for efficiency

### 3. Add Health Checks
Implement `/health` and `/readyz` endpoints

### 4. Improve Logging
Add rotating file handler and structured logging

### 5. TypeScript Frontend
Migrate to TypeScript for better type safety

### 6. Add Job Queue
Implement proper job queue like GenDJ's warp system

### 7. Cloud Deployment
Add RunPod/cloud deployment patterns from GenDJ

---

## Code Patterns to Copy

### TurboJPEG for Speed
```python
from turbojpeg import TurboJPEG, TJPF_RGB
jpeg = TurboJPEG()
frame = jpeg.decode(frame_data_np, pixel_format=TJPF_RGB)
```

### Frame Rate Control
```python
FRAME_RATE = 30
FRAME_DURATION = 1000 / FRAME_RATE
```

### Prompt Library
```typescript
const promptLibraryOptions = [
  { value: 'cyberpunk neon style', label: 'Cyberpunk' },
  { value: 'oil painting', label: 'Oil Painting' },
  // ...
];
```

### WebRTC Integration (from Scope)
```python
# Scope has full WebRTC implementation
# Can be used for Ant Media integration
```

---

## Next Steps

1. ✅ Analyze repos (DONE)
2. ⏭️ Implement settings API
3. ⏭️ Add batching to backend
4. ⏭️ Improve logging
5. ⏭️ Add health checks
6. ⏭️ Consider TypeScript migration
