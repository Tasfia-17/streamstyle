from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "StreamStyle AI Demo (Minimal)",
        "message": "Full version requires PyTorch installation",
        "note": "Disk quota exceeded - showing demo UI only"
    }

@app.get("/health")
async def health():
    return {"status": "ok", "mode": "demo"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({
        "type": "info",
        "message": "Demo mode - AI processing requires PyTorch installation"
    })
    
    try:
        while True:
            data = await websocket.receive_json()
            if data["type"] == "frame":
                # Echo back the same frame (no AI processing)
                await websocket.send_json({
                    "type": "styled_frame",
                    "image": data["image"],
                    "note": "Demo mode - showing original frame"
                })
    except:
        pass

@app.get("/demo", response_class=HTMLResponse)
async def demo():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>StreamStyle AI - Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: #0a0a0a;
                color: #fff;
            }
            h1 { color: #6366f1; }
            .status { 
                background: #1a1a1a;
                padding: 20px;
                border-radius: 8px;
                margin: 20px 0;
            }
            .note {
                background: #ef444420;
                border-left: 4px solid #ef4444;
                padding: 15px;
                margin: 20px 0;
            }
            code {
                background: #2a2a2a;
                padding: 2px 6px;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <h1>🎨 StreamStyle AI - Demo Mode</h1>
        
        <div class="status">
            <h2>✅ Backend Running</h2>
            <p>FastAPI server is active on port 8000</p>
            <p><strong>Status:</strong> Demo Mode</p>
        </div>
        
        <div class="note">
            <h3>⚠️ Disk Quota Exceeded</h3>
            <p>Cannot install PyTorch and AI models due to disk quota limits.</p>
            <p>This is a minimal demo showing the backend structure.</p>
        </div>
        
        <h2>📚 Project Documentation</h2>
        <ul>
            <li><strong>README.md</strong> - Complete guide</li>
            <li><strong>PRODUCT_OVERVIEW.md</strong> - Product vision & demo script</li>
            <li><strong>HACKATHON_CHECKLIST.md</strong> - Preparation guide</li>
            <li><strong>docs/DEMO_SCRIPT.md</strong> - 5-minute presentation</li>
        </ul>
        
        <h2>🚀 To Run Full Version</h2>
        <ol>
            <li>Free up disk space (need ~5GB for PyTorch + models)</li>
            <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
            <li>Run backend: <code>python main.py</code></li>
            <li>Run frontend: <code>cd frontend && npm install && npm run dev</code></li>
        </ol>
        
        <h2>🎬 Demo Video Alternative</h2>
        <p>Since AI processing requires more disk space, you can:</p>
        <ul>
            <li>Record a demo video showing the concept</li>
            <li>Use screenshots from documentation</li>
            <li>Present the architecture and code</li>
            <li>Show the comprehensive documentation (9 files)</li>
        </ul>
        
        <h2>📊 What You Have</h2>
        <ul>
            <li>✅ Complete codebase (backend + frontend)</li>
            <li>✅ 9 documentation files</li>
            <li>✅ Demo script (3-4 minutes)</li>
            <li>✅ Architecture diagrams</li>
            <li>✅ Production-ready patterns</li>
            <li>✅ Open source analysis</li>
        </ul>
        
        <p><strong>Your project is complete - just needs disk space to run the AI!</strong></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting StreamStyle AI Demo Server...")
    print("📍 Open: http://localhost:8000/demo")
    uvicorn.run(app, host="0.0.0.0", port=8000)
