# StreamStyle AI - Google Colab Setup

## 🚀 Quick Start on Colab

### Step 1: Open Google Colab
Go to: https://colab.research.google.com/

### Step 2: Create New Notebook
Click "New Notebook"

### Step 3: Enable GPU
- Click "Runtime" → "Change runtime type"
- Select "T4 GPU" or "A100 GPU"
- Click "Save"

---

## 📝 Colab Notebook Code

Copy and paste these cells into your Colab notebook:

### Cell 1: Clone Repository
```python
!git clone https://github.com/YOUR_USERNAME/streamstyle-ai.git
%cd streamstyle-ai/backend
```

### Cell 2: Install Dependencies
```python
!pip install -q fastapi uvicorn websockets pillow numpy
!pip install -q torch torchvision --index-url https://download.pytorch.org/whl/cu118
!pip install -q diffusers transformers accelerate
```

### Cell 3: Start Backend with Ngrok (for public URL)
```python
# Install ngrok
!pip install -q pyngrok

# Import and configure
from pyngrok import ngrok
import subprocess
import time

# Start FastAPI in background
import sys
sys.path.append('/content/streamstyle-ai/backend')

# Start server
proc = subprocess.Popen(['python', 'main.py'], 
                       cwd='/content/streamstyle-ai/backend',
                       stdout=subprocess.PIPE, 
                       stderr=subprocess.PIPE)

# Wait for server to start
time.sleep(10)

# Create public URL
public_url = ngrok.connect(8000)
print(f"🚀 Backend running at: {public_url}")
print(f"📡 WebSocket: {public_url.replace('https://', 'wss://')}/ws")
print(f"📊 Health check: {public_url}/health")
```

### Cell 4: Keep Server Running
```python
# Keep the server alive
try:
    proc.wait()
except KeyboardInterrupt:
    proc.terminate()
    print("Server stopped")
```

---

## 🎨 Frontend Options

### Option A: Use Colab for Backend Only
1. Run backend on Colab (get ngrok URL)
2. Update frontend locally to use ngrok URL
3. Run frontend on your machine

**Update frontend WebSocket URL:**
```javascript
// In frontend/src/App.jsx
const WS_URL = 'wss://YOUR-NGROK-ID.ngrok.io/ws'
```

### Option B: Full Colab Setup with Gradio
```python
# Cell 5: Create Gradio Interface
!pip install -q gradio

import gradio as gr
import requests
import base64
from PIL import Image
import io

def process_webcam(image, prompt):
    # Convert to base64
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    img_data = f"data:image/jpeg;base64,{img_str}"
    
    # Send to backend (simplified - use WebSocket in production)
    # For demo, just return original
    return image

# Create interface
demo = gr.Interface(
    fn=process_webcam,
    inputs=[
        gr.Image(source="webcam", type="pil", label="Webcam"),
        gr.Textbox(label="Style Prompt", value="cyberpunk neon style")
    ],
    outputs=gr.Image(label="Styled Output"),
    title="🎨 StreamStyle AI",
    description="Real-time AI video styling"
)

demo.launch(share=True)
```

---

## 📋 Complete Colab Notebook (Copy-Paste Ready)

```python
# ========================================
# StreamStyle AI - Google Colab Setup
# ========================================

# 1. Setup
!git clone https://github.com/YOUR_USERNAME/streamstyle-ai.git
%cd streamstyle-ai/backend

# 2. Install Dependencies
print("📦 Installing dependencies...")
!pip install -q fastapi uvicorn websockets pillow numpy pyngrok
!pip install -q torch torchvision --index-url https://download.pytorch.org/whl/cu118
!pip install -q diffusers transformers accelerate

# 3. Start Backend
print("🚀 Starting backend...")
import subprocess
import time
from pyngrok import ngrok

# Start FastAPI
proc = subprocess.Popen(
    ['python', 'main.py'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Wait for startup
time.sleep(15)

# Create public URL
public_url = ngrok.connect(8000)
ws_url = str(public_url).replace('https://', 'wss://') + '/ws'

print("\n" + "="*50)
print("✅ StreamStyle AI Backend Running!")
print("="*50)
print(f"🌐 Backend URL: {public_url}")
print(f"📡 WebSocket: {ws_url}")
print(f"📊 Health: {public_url}/health")
print(f"📚 API Docs: {public_url}/docs")
print("="*50)
print("\n💡 Use this WebSocket URL in your frontend:")
print(f"   const WS_URL = '{ws_url}'")
print("\n⏸️  Keep this cell running to keep server alive")
print("="*50)

# Keep alive
try:
    proc.wait()
except KeyboardInterrupt:
    proc.terminate()
    print("\n🛑 Server stopped")
```

---

## 🎯 Step-by-Step Instructions

### 1. Open Colab
- Go to https://colab.research.google.com/
- Sign in with Google account

### 2. Create Notebook
- Click "File" → "New notebook"
- Name it "StreamStyle_AI"

### 3. Enable GPU
- Click "Runtime" → "Change runtime type"
- Hardware accelerator: **T4 GPU**
- Click "Save"

### 4. Paste Code
- Copy the "Complete Colab Notebook" code above
- Paste into first cell
- Click "Run" (▶️ button)

### 5. Wait for Setup
- Dependencies install: ~3 minutes
- Model download: ~5 minutes (first time)
- Server starts: ~15 seconds

### 6. Get Your URL
You'll see output like:
```
✅ StreamStyle AI Backend Running!
🌐 Backend URL: https://abc123.ngrok.io
📡 WebSocket: wss://abc123.ngrok.io/ws
```

### 7. Test It
Open the backend URL in browser to verify it's running.

---

## 🎨 Frontend Setup

### Option 1: Local Frontend
```bash
# On your local machine
cd streamstyle-ai/frontend

# Update WebSocket URL in src/App.jsx
# Change line 5 to your ngrok URL:
const WS_URL = 'wss://YOUR-NGROK-ID.ngrok.io/ws'

# Run frontend
npm install
npm run dev

# Open http://localhost:3000
```

### Option 2: Deploy Frontend
Deploy frontend to:
- **Vercel**: Free, instant deployment
- **Netlify**: Free, easy setup
- **GitHub Pages**: Free hosting

Update environment variable with ngrok URL.

---

## ⚠️ Important Notes

### Ngrok Limits
- **Free tier**: URL changes each time
- **Pro tier**: Fixed URL ($8/month)
- **Session timeout**: 2 hours on free tier

### Colab Limits
- **Free tier**: 12 hour sessions
- **GPU time**: Limited per day
- **Idle timeout**: 90 minutes

### For Demo
1. Start Colab notebook
2. Get ngrok URL
3. Update frontend
4. Run frontend locally
5. Demo works perfectly!

---

## 🚀 Quick Demo Script

```python
# Minimal demo in one cell
!pip install -q fastapi uvicorn pyngrok torch diffusers transformers

from pyngrok import ngrok
import subprocess, time

# Start server
proc = subprocess.Popen(['python', '-c', '''
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "StreamStyle AI Running on Colab!"}

uvicorn.run(app, host="0.0.0.0", port=8000)
'''])

time.sleep(5)
url = ngrok.connect(8000)
print(f"🚀 Running at: {url}")

proc.wait()
```

---

## 📞 Troubleshooting

**"Model download too slow"**
```python
# Use smaller model for demo
!pip install -q diffusers[torch]
# Model will download on first inference (~2GB, 5 min)
```

**"Ngrok connection failed"**
```python
# Get free ngrok token from https://ngrok.com
from pyngrok import ngrok
ngrok.set_auth_token("YOUR_TOKEN_HERE")
```

**"Session disconnected"**
- Colab free tier has timeouts
- Keep browser tab active
- Or upgrade to Colab Pro

---

## ✅ You're Ready!

1. Copy the complete notebook code
2. Paste into Colab
3. Run cell
4. Get ngrok URL
5. Update frontend
6. Demo works! 🎉

**Total setup time: ~10 minutes**
