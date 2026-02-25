<div align="center">

<!-- Logo SVG -->
<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
  </defs>
  <circle cx="100" cy="100" r="90" fill="url(#grad1)" opacity="0.2"/>
  <path d="M 60 80 Q 100 60 140 80" stroke="url(#grad1)" stroke-width="8" fill="none" stroke-linecap="round"/>
  <circle cx="70" cy="90" r="12" fill="url(#grad1)"/>
  <circle cx="130" cy="90" r="12" fill="url(#grad1)"/>
  <path d="M 70 130 Q 100 150 130 130" stroke="url(#grad1)" stroke-width="8" fill="none" stroke-linecap="round"/>
  <circle cx="100" cy="100" r="60" stroke="url(#grad1)" stroke-width="4" fill="none" opacity="0.5"/>
</svg>

# 🎨 StreamStyle AI

**Real-time AI-powered streaming platform that transforms live video into artistic visuals**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![React 18](https://img.shields.io/badge/react-18-blue.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)](https://fastapi.tiangolo.com/)

[Demo](#-demo) • [Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Architecture](#-architecture)

</div>

---

## 🌟 What Is It?

**StreamStyle AI** transforms your webcam into an AI art studio in real-time. Type any artistic style, and watch your video transform instantly using Stable Diffusion Turbo.

```
Normal Webcam → Type "cyberpunk neon" → ✨ BOOM ✨ → AI-styled stream
```

**Inspired by**: [GenDJ](https://github.com/GenDJ) - Open source real-time AI warping  
**Our innovation**: Voice control + 8 presets + production-ready architecture

---

## ✨ Features

<div align="center">

<!-- Features SVG -->
<svg width="600" height="150" viewBox="0 0 600 150" xmlns="http://www.w3.org/2000/svg">
  <!-- Webcam Icon -->
  <g transform="translate(50, 50)">
    <rect x="10" y="10" width="60" height="50" rx="5" fill="#667eea" opacity="0.3"/>
    <circle cx="40" cy="35" r="15" fill="#667eea"/>
    <text x="40" y="90" text-anchor="middle" font-size="12" fill="#fff">Live Video</text>
  </g>
  
  <!-- AI Icon -->
  <g transform="translate(200, 50)">
    <circle cx="40" cy="35" r="25" fill="#764ba2" opacity="0.3"/>
    <path d="M 30 25 L 40 35 L 50 25 M 30 45 L 40 35 L 50 45" stroke="#764ba2" stroke-width="3" fill="none"/>
    <text x="40" y="90" text-anchor="middle" font-size="12" fill="#fff">AI Transform</text>
  </g>
  
  <!-- Voice Icon -->
  <g transform="translate(350, 50)">
    <ellipse cx="40" cy="30" rx="15" ry="20" fill="#10b981" opacity="0.3"/>
    <rect x="35" y="50" width="10" height="10" fill="#10b981"/>
    <text x="40" y="90" text-anchor="middle" font-size="12" fill="#fff">Voice Control</text>
  </g>
  
  <!-- Stream Icon -->
  <g transform="translate(500, 50)">
    <circle cx="40" cy="35" r="20" fill="#ef4444" opacity="0.3"/>
    <circle cx="40" cy="35" r="15" fill="#ef4444" opacity="0.5"/>
    <circle cx="40" cy="35" r="10" fill="#ef4444"/>
    <text x="40" y="90" text-anchor="middle" font-size="12" fill="#fff">Broadcast</text>
  </g>
</svg>

</div>

### Core Features
- 🎥 **Live Video Processing** - 640x480 @ 5 FPS
- 🤖 **AI Transformation** - Stable Diffusion Turbo (1-step inference)
- ⚡ **Real-Time** - <1s latency on GPU, 2-3s on CPU
- 🎨 **8 Style Presets** - One-click transformations
- 🎤 **Voice Control** - Say "anime mode" to change styles
- 📊 **Live Monitoring** - FPS counter, status indicators
- 📡 **Broadcast Ready** - Ant Media WebRTC integration

### Advanced Features
- ✅ Custom prompts (unlimited creativity)
- ✅ Settings API (RESTful controls)
- ✅ Health checks (production monitoring)
- ✅ Rotating logs (disk management)
- ✅ GPU optimization (torch.compile, float16)
- ✅ Queue management (prevents backlog)

---

## 🎬 Demo

### Perfect Demo Flow (3-4 Minutes)

1. **Start Streaming** → Show webcam feed
2. **Type "cyberpunk neon"** → AI transforms video
3. **Click "Van Gogh" preset** → Style changes instantly
4. **Say "pixel art"** → Voice control in action
5. **Show viewer page** → Multiple people watching

**Demo time:** 20 seconds to wow judges 🤯

---

## 🚀 Quick Start

### One Command
```bash
cd streamstyle-ai
./start.sh
```

Then open: **http://localhost:3000**

### Manual Setup

**Backend:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**First run:** Model downloads ~2GB (5-10 minutes)

---

## 🎨 Style Presets

<div align="center">

| Preset | Example | Best For |
|--------|---------|----------|
| 🌃 Cyberpunk | Neon lights, futuristic | Sci-fi streams |
| 🎨 Oil Painting | Classic brushstrokes | Artistic look |
| 🎌 Anime | Manga style | Cartoon effect |
| 🌊 Watercolor | Soft, dreamy | Gentle aesthetic |
| 🎮 Pixel Art | 8-bit retro | Gaming streams |
| 🖼️ Van Gogh | Impressionist | Famous artist |
| ✏️ Sketch | Hand-drawn | Minimalist |
| 💥 Pop Art | Bold colors | Comic book |

</div>

---

## 🏗 Architecture

<div align="center">

<!-- Architecture Diagram SVG -->
<svg width="700" height="400" viewBox="0 0 700 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Frontend Box -->
  <rect x="50" y="50" width="250" height="120" rx="10" fill="#667eea" opacity="0.2" stroke="#667eea" stroke-width="2"/>
  <text x="175" y="80" text-anchor="middle" font-size="16" font-weight="bold" fill="#667eea">FRONTEND</text>
  <text x="175" y="105" text-anchor="middle" font-size="12" fill="#fff">React + Vite</text>
  <text x="175" y="125" text-anchor="middle" font-size="12" fill="#fff">Webcam Capture</text>
  <text x="175" y="145" text-anchor="middle" font-size="12" fill="#fff">WebSocket Client</text>
  
  <!-- Arrow -->
  <path d="M 300 110 L 380 110" stroke="#10b981" stroke-width="3" marker-end="url(#arrowhead)"/>
  <text x="340" y="100" text-anchor="middle" font-size="11" fill="#10b981">WebSocket</text>
  
  <!-- Backend Box -->
  <rect x="400" y="50" width="250" height="120" rx="10" fill="#764ba2" opacity="0.2" stroke="#764ba2" stroke-width="2"/>
  <text x="525" y="80" text-anchor="middle" font-size="16" font-weight="bold" fill="#764ba2">BACKEND</text>
  <text x="525" y="105" text-anchor="middle" font-size="12" fill="#fff">FastAPI + Python</text>
  <text x="525" y="125" text-anchor="middle" font-size="12" fill="#fff">Async Processing</text>
  <text x="525" y="145" text-anchor="middle" font-size="12" fill="#fff">Queue Management</text>
  
  <!-- Arrow Down -->
  <path d="M 525 170 L 525 220" stroke="#10b981" stroke-width="3" marker-end="url(#arrowhead)"/>
  
  <!-- AI Box -->
  <rect x="400" y="230" width="250" height="120" rx="10" fill="#ef4444" opacity="0.2" stroke="#ef4444" stroke-width="2"/>
  <text x="525" y="260" text-anchor="middle" font-size="16" font-weight="bold" fill="#ef4444">AI MODEL</text>
  <text x="525" y="285" text-anchor="middle" font-size="12" fill="#fff">Stable Diffusion Turbo</text>
  <text x="525" y="305" text-anchor="middle" font-size="12" fill="#fff">512x512 @ 1-step</text>
  <text x="525" y="325" text-anchor="middle" font-size="12" fill="#fff">GPU/CPU Support</text>
  
  <!-- Arrow Back -->
  <path d="M 400 290 L 320 290 L 320 110 L 300 110" stroke="#10b981" stroke-width="3" marker-end="url(#arrowhead)"/>
  <text x="310" y="200" text-anchor="middle" font-size="11" fill="#10b981" transform="rotate(-90 310 200)">Styled Frames</text>
  
  <!-- Ant Media Box -->
  <rect x="50" y="230" width="250" height="80" rx="10" fill="#10b981" opacity="0.2" stroke="#10b981" stroke-width="2"/>
  <text x="175" y="260" text-anchor="middle" font-size="16" font-weight="bold" fill="#10b981">ANT MEDIA</text>
  <text x="175" y="285" text-anchor="middle" font-size="12" fill="#fff">WebRTC Broadcast</text>
  
  <!-- Arrow Marker -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#10b981" />
    </marker>
  </defs>
</svg>

</div>

### System Flow

```
Webcam (640x480) → Frame Queue (200ms) → WebSocket → Backend
                                                        ↓
                                                   AI Processing
                                                   (SD Turbo)
                                                        ↓
Styled Display ← Canvas Draw ← WebSocket ← Styled Frames
     ↓
Ant Media Broadcast → Viewers
```

---

## 📊 Performance

| Metric | GPU (CUDA) | CPU |
|--------|------------|-----|
| Processing Time | 0.3-0.8s | 2-5s |
| FPS Output | 1-3 FPS | 0.2-0.5 FPS |
| Latency | <1s | 2-3s |
| Memory | 3-4GB VRAM | 4GB RAM |
| Resolution | 512x512 | 512x512 |

---

## 📚 Documentation

- [Product Overview](PRODUCT_OVERVIEW.md) - Complete product vision
- [Hackathon Checklist](HACKATHON_CHECKLIST.md) - Demo preparation
- [Architecture](docs/ARCHITECTURE.md) - System design
- [Demo Script](docs/DEMO_SCRIPT.md) - 5-minute presentation
- [Ant Media Integration](docs/ANT_MEDIA_INTEGRATION.md) - Broadcasting
- [Colab Setup](COLAB_SETUP.md) - Run on Google Colab
- [GenDJ Insights](docs/GENDJ_INSIGHTS.md) - Open source analysis

---

## 🎯 Use Cases

<div align="center">

<!-- Use Cases SVG -->
<svg width="600" height="200" viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(100, 50)">
    <circle cx="0" cy="0" r="30" fill="#667eea" opacity="0.3"/>
    <text x="0" y="5" text-anchor="middle" font-size="24">🎮</text>
    <text x="0" y="50" text-anchor="middle" font-size="12" fill="#fff">Gaming</text>
    <text x="0" y="65" text-anchor="middle" font-size="12" fill="#fff">Streams</text>
  </g>
  
  <g transform="translate(250, 50)">
    <circle cx="0" cy="0" r="30" fill="#764ba2" opacity="0.3"/>
    <text x="0" y="5" text-anchor="middle" font-size="24">🎵</text>
    <text x="0" y="50" text-anchor="middle" font-size="12" fill="#fff">Music</text>
    <text x="0" y="65" text-anchor="middle" font-size="12" fill="#fff">Performances</text>
  </g>
  
  <g transform="translate(400, 50)">
    <circle cx="0" cy="0" r="30" fill="#10b981" opacity="0.3"/>
    <text x="0" y="5" text-anchor="middle" font-size="24">🎭</text>
    <text x="0" y="50" text-anchor="middle" font-size="12" fill="#fff">Live</text>
    <text x="0" y="65" text-anchor="middle" font-size="12" fill="#fff">Events</text>
  </g>
  
  <g transform="translate(100, 150)">
    <circle cx="0" cy="0" r="30" fill="#ef4444" opacity="0.3"/>
    <text x="0" y="5" text-anchor="middle" font-size="24">🛍️</text>
    <text x="0" y="50" text-anchor="middle" font-size="12" fill="#fff">Live</text>
    <text x="0" y="65" text-anchor="middle" font-size="12" fill="#fff">Shopping</text>
  </g>
  
  <g transform="translate(250, 150)">
    <circle cx="0" cy="0" r="30" fill="#8b5cf6" opacity="0.3"/>
    <text x="0" y="5" text-anchor="middle" font-size="24">📚</text>
    <text x="0" y="50" text-anchor="middle" font-size="12" fill="#fff">Education</text>
    <text x="0" y="65" text-anchor="middle" font-size="12" fill="#fff">Content</text>
  </g>
  
  <g transform="translate(400, 150)">
    <circle cx="0" cy="0" r="30" fill="#f59e0b" opacity="0.3"/>
    <text x="0" y="5" text-anchor="middle" font-size="24">🎨</text>
    <text x="0" y="50" text-anchor="middle" font-size="12" fill="#fff">Art</text>
    <text x="0" y="65" text-anchor="middle" font-size="12" fill="#fff">Streams</text>
  </g>
</svg>

</div>

---

## 🛠 Tech Stack

**Frontend:**
- React 18
- Vite
- WebSocket API
- Web Speech API
- Canvas API

**Backend:**
- FastAPI
- PyTorch 2.2+
- Diffusers
- Stable Diffusion Turbo
- WebSocket

**Streaming:**
- Ant Media Server
- WebRTC

---

## 🔧 Configuration

### Adjust Frame Rate
```javascript
// frontend/src/App.jsx line 95
setInterval(() => captureAndSendFrame(), 200)  // 200ms = 5 FPS
```

### Adjust Resolution
```python
# backend/main.py line 52
image = image.resize((512, 512))  # Try 256 or 768
```

### Adjust AI Strength
```python
# backend/main.py line 57
strength=0.5,  # 0.0-1.0 (lower = more original)
```

---

## 🐛 Troubleshooting

**Model download slow:**
```bash
export HF_HOME=/tmp/huggingface
```

**WebSocket error:**
```bash
curl http://localhost:8000/health
```

**Camera not working:**
- Grant browser permissions
- Check camera isn't used by another app

**Slow processing:**
- Normal on CPU (2-5s)
- Check GPU: `python -c "import torch; print(torch.cuda.is_available())"`

---

## 🏆 Why This Project Wins

1. ✅ **Works Reliably** - Tested on CPU and GPU
2. ✅ **Visually Impressive** - 8 stunning styles
3. ✅ **Low Latency** - <1s with GPU
4. ✅ **Interactive** - Voice control
5. ✅ **Scalable** - Ant Media ready
6. ✅ **Well-Documented** - 9 comprehensive guides
7. ✅ **Production-Ready** - Health checks, logging
8. ✅ **Clear Use Case** - Content creators need this

---

## 💼 Market Positioning

### Elevator Pitch
> "Content creators struggle to stand out visually. StreamStyle AI lets creators transform their live streams into immersive AI art experiences instantly — no editing, no delays, just real-time magic."

### Target Users
- Twitch/YouTube streamers
- VJs & live performers
- Virtual event hosts
- Content creators
- Live shopping hosts

---

## 🗺️ Roadmap

### Current (v1.0)
- ✅ Real-time AI transformation
- ✅ 8 style presets
- ✅ Voice control
- ✅ WebSocket streaming
- ✅ Ant Media integration ready

### Future (v2.0)
- [ ] Frame consistency (latent blending)
- [ ] MIDI controller support
- [ ] Live parameter sliders
- [ ] Green screen integration
- [ ] Higher FPS optimization
- [ ] Mobile app (React Native)

---

## 📝 License

MIT License - Free for hackathon and commercial use

---

## 🙏 Credits

- **Stable Diffusion Turbo** by Stability AI
- **FastAPI** by Sebastián Ramírez
- **React** by Meta
- **Ant Media Server** by Ant Media
- Inspired by **GenDJ** and **Scope** (open source)

---

## 📞 Support

**Quick Commands:**
```bash
./start.sh          # Start everything
./help.sh           # Show all commands
curl localhost:8000/health  # Check backend
```

**Links:**
- [Documentation](docs/)
- [Issues](https://github.com/Tasfia-17/streamstyle/issues)
- [Discussions](https://github.com/Tasfia-17/streamstyle/discussions)

---

<div align="center">

**🎨 Built for hackathons. Optimized for demos. Ready to win. 🚀**

**Demo time: 3-4 minutes | Setup time: 5 minutes | Wow factor: 🤯**

---

Made with 💜 by [Tasfia](https://github.com/Tasfia-17)

⭐ Star this repo if you find it helpful!

</div>
