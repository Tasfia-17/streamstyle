<div align="center">

<!-- Logo SVG -->
<svg width="280" height="280" viewBox="0 0 280 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#764ba2;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#f093fb;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Outer glow circle -->
  <circle cx="140" cy="140" r="120" fill="url(#grad1)" opacity="0.15"/>
  <circle cx="140" cy="140" r="100" fill="none" stroke="url(#grad1)" stroke-width="3" opacity="0.4" stroke-dasharray="5,5">
    <animateTransform attributeName="transform" type="rotate" from="0 140 140" to="360 140 140" dur="20s" repeatCount="indefinite"/>
  </circle>
  
  <!-- Camera body -->
  <rect x="80" y="100" width="120" height="80" rx="15" fill="url(#grad1)" opacity="0.9" filter="url(#glow)"/>
  <rect x="85" y="105" width="110" height="70" rx="12" fill="#1a1a2e" opacity="0.8"/>
  
  <!-- Camera lens -->
  <circle cx="140" cy="140" r="35" fill="url(#grad2)" opacity="0.3"/>
  <circle cx="140" cy="140" r="30" fill="none" stroke="url(#grad2)" stroke-width="4"/>
  <circle cx="140" cy="140" r="20" fill="url(#grad1)" opacity="0.6">
    <animate attributeName="r" values="20;22;20" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="140" cy="140" r="12" fill="#fff" opacity="0.8"/>
  
  <!-- Lens reflection -->
  <ellipse cx="135" cy="135" rx="8" ry="10" fill="#fff" opacity="0.6" transform="rotate(-45 135 135)"/>
  
  <!-- Camera details -->
  <circle cx="175" cy="115" r="6" fill="#ef4444" opacity="0.9">
    <animate attributeName="opacity" values="0.9;0.3;0.9" dur="1.5s" repeatCount="indefinite"/>
  </circle>
  <rect x="95" y="115" width="25" height="8" rx="4" fill="url(#grad2)" opacity="0.7"/>
  
  <!-- AI sparkles -->
  <g opacity="0.8">
    <path d="M 60 80 L 65 85 L 60 90 L 55 85 Z" fill="#fbbf24">
      <animate attributeName="opacity" values="0.8;0.3;0.8" dur="1s" repeatCount="indefinite"/>
    </path>
    <path d="M 220 80 L 225 85 L 220 90 L 215 85 Z" fill="#fbbf24">
      <animate attributeName="opacity" values="0.3;0.8;0.3" dur="1s" repeatCount="indefinite"/>
    </path>
    <path d="M 70 180 L 75 185 L 70 190 L 65 185 Z" fill="#a78bfa">
      <animate attributeName="opacity" values="0.8;0.3;0.8" dur="1.2s" repeatCount="indefinite"/>
    </path>
    <path d="M 210 180 L 215 185 L 210 190 L 205 185 Z" fill="#a78bfa">
      <animate attributeName="opacity" values="0.3;0.8;0.3" dur="1.2s" repeatCount="indefinite"/>
    </path>
  </g>
  
  <!-- Streaming waves -->
  <g opacity="0.6">
    <path d="M 140 200 Q 120 210 100 200" stroke="url(#grad2)" stroke-width="3" fill="none" stroke-linecap="round">
      <animate attributeName="opacity" values="0.6;0.2;0.6" dur="2s" repeatCount="indefinite"/>
    </path>
    <path d="M 140 210 Q 115 225 90 210" stroke="url(#grad2)" stroke-width="3" fill="none" stroke-linecap="round">
      <animate attributeName="opacity" values="0.4;0.1;0.4" dur="2s" begin="0.3s" repeatCount="indefinite"/>
    </path>
    <path d="M 140 200 Q 160 210 180 200" stroke="url(#grad2)" stroke-width="3" fill="none" stroke-linecap="round">
      <animate attributeName="opacity" values="0.6;0.2;0.6" dur="2s" repeatCount="indefinite"/>
    </path>
    <path d="M 140 210 Q 165 225 190 210" stroke="url(#grad2)" stroke-width="3" fill="none" stroke-linecap="round">
      <animate attributeName="opacity" values="0.4;0.1;0.4" dur="2s" begin="0.3s" repeatCount="indefinite"/>
    </path>
  </g>
  
  <!-- Magic wand -->
  <g transform="translate(200, 60)">
    <line x1="0" y1="0" x2="20" y2="20" stroke="url(#grad1)" stroke-width="3" stroke-linecap="round"/>
    <path d="M 22 18 L 26 22 L 22 26 L 18 22 Z" fill="#fbbf24" filter="url(#glow)">
      <animateTransform attributeName="transform" type="rotate" from="0 22 22" to="360 22 22" dur="3s" repeatCount="indefinite"/>
    </path>
  </g>
</svg>

# StreamStyle AI

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

## Features

<div align="center">

<!-- Features SVG -->
<svg width="800" height="200" viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="featGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="featGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#10b981;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#059669;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="featGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ef4444;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#dc2626;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="featGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f59e0b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#d97706;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Webcam Icon -->
  <g transform="translate(100, 60)">
    <circle cx="0" cy="0" r="45" fill="url(#featGrad1)" opacity="0.2"/>
    <rect x="-25" y="-20" width="50" height="35" rx="8" fill="url(#featGrad1)" opacity="0.8"/>
    <rect x="-20" y="-15" width="40" height="25" rx="5" fill="#1a1a2e"/>
    <circle cx="0" cy="-2" r="12" fill="url(#featGrad1)" opacity="0.6"/>
    <circle cx="0" cy="-2" r="8" fill="#fff" opacity="0.8"/>
    <circle cx="-3" cy="-5" r="3" fill="#fff" opacity="0.9"/>
    <circle cx="12" cy="-12" r="3" fill="#ef4444">
      <animate attributeName="opacity" values="1;0.3;1" dur="1.5s" repeatCount="indefinite"/>
    </circle>
    <rect x="-15" y="20" width="30" height="4" rx="2" fill="url(#featGrad1)" opacity="0.6"/>
    <text x="0" y="65" text-anchor="middle" font-size="14" font-weight="bold" fill="#667eea">Live Video</text>
    <text x="0" y="82" text-anchor="middle" font-size="11" fill="#9ca3af">640x480 @ 5 FPS</text>
  </g>
  
  <!-- AI Transform Icon -->
  <g transform="translate(300, 60)">
    <circle cx="0" cy="0" r="45" fill="url(#featGrad1)" opacity="0.2"/>
    <circle cx="0" cy="0" r="30" fill="url(#featGrad1)" opacity="0.3"/>
    <circle cx="-15" cy="-10" r="8" fill="url(#featGrad1)"/>
    <circle cx="15" cy="-10" r="8" fill="url(#featGrad1)"/>
    <circle cx="0" cy="12" r="8" fill="url(#featGrad1)"/>
    <circle cx="-12" cy="8" r="6" fill="#764ba2" opacity="0.7"/>
    <circle cx="12" cy="8" r="6" fill="#764ba2" opacity="0.7"/>
    <line x1="-15" y1="-10" x2="0" y2="12" stroke="#667eea" stroke-width="2" opacity="0.6"/>
    <line x1="15" y1="-10" x2="0" y2="12" stroke="#667eea" stroke-width="2" opacity="0.6"/>
    <circle cx="0" cy="0" r="3" fill="#fbbf24">
      <animate attributeName="r" values="3;6;3" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="0" y="65" text-anchor="middle" font-size="14" font-weight="bold" fill="#764ba2">AI Transform</text>
    <text x="0" y="82" text-anchor="middle" font-size="11" fill="#9ca3af">SD Turbo 1-step</text>
  </g>
  
  <!-- Voice Control Icon -->
  <g transform="translate(500, 60)">
    <circle cx="0" cy="0" r="45" fill="url(#featGrad2)" opacity="0.2"/>
    <ellipse cx="0" cy="-5" rx="12" ry="18" fill="url(#featGrad2)" opacity="0.8"/>
    <rect x="-3" y="13" width="6" height="8" rx="1" fill="url(#featGrad2)" opacity="0.8"/>
    <path d="M -15 8 Q -15 -5 -12 -5" stroke="url(#featGrad2)" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.6">
      <animate attributeName="opacity" values="0.6;0.2;0.6" dur="1.5s" repeatCount="indefinite"/>
    </path>
    <path d="M 15 8 Q 15 -5 12 -5" stroke="url(#featGrad2)" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.6">
      <animate attributeName="opacity" values="0.6;0.2;0.6" dur="1.5s" begin="0.3s" repeatCount="indefinite"/>
    </path>
    <path d="M -20 12 Q -20 -8 -15 -8" stroke="url(#featGrad2)" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.4">
      <animate attributeName="opacity" values="0.4;0.1;0.4" dur="1.5s" begin="0.6s" repeatCount="indefinite"/>
    </path>
    <path d="M 20 12 Q 20 -8 15 -8" stroke="url(#featGrad2)" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.4">
      <animate attributeName="opacity" values="0.4;0.1;0.4" dur="1.5s" begin="0.9s" repeatCount="indefinite"/>
    </path>
    <path d="M -10 21 L 0 28 L 10 21" stroke="url(#featGrad2)" stroke-width="3" fill="none" stroke-linecap="round"/>
    <text x="0" y="65" text-anchor="middle" font-size="14" font-weight="bold" fill="#10b981">Voice Control</text>
    <text x="0" y="82" text-anchor="middle" font-size="11" fill="#9ca3af">Web Speech API</text>
  </g>
  
  <!-- Broadcast Icon -->
  <g transform="translate(700, 60)">
    <circle cx="0" cy="0" r="45" fill="url(#featGrad3)" opacity="0.2"/>
    <circle cx="0" cy="0" r="25" fill="url(#featGrad3)" opacity="0.3">
      <animate attributeName="r" values="25;35;25" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.3;0;0.3" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="18" fill="url(#featGrad3)" opacity="0.5">
      <animate attributeName="r" values="18;28;18" dur="2s" begin="0.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.5;0;0.5" dur="2s" begin="0.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="12" fill="url(#featGrad3)"/>
    <circle cx="0" cy="0" r="6" fill="#fff" opacity="0.9">
      <animate attributeName="opacity" values="0.9;0.5;0.9" dur="1s" repeatCount="indefinite"/>
    </circle>
    <text x="0" y="65" text-anchor="middle" font-size="14" font-weight="bold" fill="#ef4444">Broadcast</text>
    <text x="0" y="82" text-anchor="middle" font-size="11" fill="#9ca3af">WebRTC Ready</text>
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

## Architecture

<div align="center">

<!-- Architecture Diagram SVG -->
<svg width="900" height="550" viewBox="0 0 900 550" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="archGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="archGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#10b981;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#059669;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="archGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ef4444;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#dc2626;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="archGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f59e0b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#d97706;stop-opacity:1" />
    </linearGradient>
    <marker id="arrowGreen" markerWidth="12" markerHeight="12" refX="11" refY="6" orient="auto">
      <polygon points="0 0, 12 6, 0 12" fill="#10b981" />
    </marker>
    <marker id="arrowPurple" markerWidth="12" markerHeight="12" refX="11" refY="6" orient="auto">
      <polygon points="0 0, 12 6, 0 12" fill="#764ba2" />
    </marker>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- User/Browser Section -->
  <g transform="translate(100, 80)">
    <rect x="0" y="0" width="280" height="160" rx="15" fill="url(#archGrad1)" opacity="0.15" stroke="url(#archGrad1)" stroke-width="3" filter="url(#shadow)"/>
    <text x="140" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#667eea">FRONTEND</text>
    <text x="140" y="55" text-anchor="middle" font-size="13" fill="#9ca3af">React 18 + Vite</text>
    
    <!-- Webcam icon -->
    <g transform="translate(50, 75)">
      <rect x="0" y="0" width="50" height="40" rx="8" fill="#667eea" opacity="0.3"/>
      <circle cx="25" cy="20" r="12" fill="#667eea"/>
      <circle cx="25" cy="20" r="6" fill="#fff" opacity="0.8"/>
      <text x="25" y="60" text-anchor="middle" font-size="11" fill="#d1d5db">Webcam</text>
    </g>
    
    <!-- WebSocket icon -->
    <g transform="translate(115, 75)">
      <circle cx="25" cy="20" r="20" fill="#10b981" opacity="0.3"/>
      <path d="M 15 15 L 25 20 L 35 15 M 15 25 L 25 20 L 35 25" stroke="#10b981" stroke-width="3" fill="none"/>
      <text x="25" y="60" text-anchor="middle" font-size="11" fill="#d1d5db">WebSocket</text>
    </g>
    
    <!-- Canvas icon -->
    <g transform="translate(180, 75)">
      <rect x="5" y="5" width="40" height="30" rx="4" fill="#764ba2" opacity="0.3" stroke="#764ba2" stroke-width="2"/>
      <rect x="10" y="10" width="12" height="12" fill="#fbbf24" opacity="0.6"/>
      <rect x="23" y="10" width="12" height="12" fill="#ef4444" opacity="0.6"/>
      <rect x="10" y="23" width="12" height="7" fill="#10b981" opacity="0.6"/>
      <text x="25" y="60" text-anchor="middle" font-size="11" fill="#d1d5db">Canvas</text>
    </g>
  </g>
  
  <!-- Arrow to Backend -->
  <g>
    <path d="M 380 160 L 480 160" stroke="url(#archGrad2)" stroke-width="4" marker-end="url(#arrowGreen)" opacity="0.8">
      <animate attributeName="stroke-dasharray" values="0,400;400,0" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="stroke-dashoffset" values="0;-400" dur="2s" repeatCount="indefinite"/>
    </path>
    <text x="430" y="145" text-anchor="middle" font-size="12" font-weight="bold" fill="#10b981">Base64 Frames</text>
    <text x="430" y="180" text-anchor="middle" font-size="11" fill="#9ca3af">WebSocket</text>
  </g>
  
  <!-- Backend Section -->
  <g transform="translate(520, 80)">
    <rect x="0" y="0" width="280" height="160" rx="15" fill="url(#archGrad1)" opacity="0.15" stroke="#764ba2" stroke-width="3" filter="url(#shadow)"/>
    <text x="140" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#764ba2">BACKEND</text>
    <text x="140" y="55" text-anchor="middle" font-size="13" fill="#9ca3af">FastAPI + Python 3.9+</text>
    
    <!-- FastAPI icon -->
    <g transform="translate(40, 75)">
      <circle cx="25" cy="20" r="20" fill="#764ba2" opacity="0.3"/>
      <path d="M 15 20 L 25 10 L 35 20 L 25 30 Z" fill="#764ba2"/>
      <text x="25" y="60" text-anchor="middle" font-size="11" fill="#d1d5db">FastAPI</text>
    </g>
    
    <!-- Queue icon -->
    <g transform="translate(110, 75)">
      <rect x="5" y="10" width="15" height="20" rx="3" fill="#f59e0b" opacity="0.6"/>
      <rect x="20" y="10" width="15" height="20" rx="3" fill="#f59e0b" opacity="0.8"/>
      <rect x="35" y="10" width="15" height="20" rx="3" fill="#f59e0b"/>
      <text x="27" y="60" text-anchor="middle" font-size="11" fill="#d1d5db">Queue</text>
    </g>
    
    <!-- Async icon -->
    <g transform="translate(185, 75)">
      <circle cx="15" cy="20" r="8" fill="#10b981" opacity="0.6">
        <animate attributeName="cy" values="20;15;20" dur="1s" repeatCount="indefinite"/>
      </circle>
      <circle cx="30" cy="20" r="8" fill="#10b981" opacity="0.8">
        <animate attributeName="cy" values="20;15;20" dur="1s" begin="0.3s" repeatCount="indefinite"/>
      </circle>
      <circle cx="45" cy="20" r="8" fill="#10b981">
        <animate attributeName="cy" values="20;15;20" dur="1s" begin="0.6s" repeatCount="indefinite"/>
      </circle>
      <text x="30" y="60" text-anchor="middle" font-size="11" fill="#d1d5db">Async</text>
    </g>
  </g>
  
  <!-- Arrow to AI Model -->
  <g>
    <path d="M 660 240 L 660 310" stroke="url(#archGrad3)" stroke-width="4" marker-end="url(#arrowGreen)" opacity="0.8">
      <animate attributeName="stroke-dasharray" values="0,200;200,0" dur="1.5s" repeatCount="indefinite"/>
      <animate attributeName="stroke-dashoffset" values="0;-200" dur="1.5s" repeatCount="indefinite"/>
    </path>
    <text x="710" y="275" text-anchor="start" font-size="12" font-weight="bold" fill="#ef4444">Image + Prompt</text>
  </g>
  
  <!-- AI Model Section -->
  <g transform="translate(520, 320)">
    <rect x="0" y="0" width="280" height="160" rx="15" fill="url(#archGrad3)" opacity="0.15" stroke="url(#archGrad3)" stroke-width="3" filter="url(#shadow)"/>
    <text x="140" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#ef4444">AI MODEL</text>
    <text x="140" y="55" text-anchor="middle" font-size="13" fill="#9ca3af">Stable Diffusion Turbo</text>
    
    <!-- GPU icon -->
    <g transform="translate(35, 75)">
      <rect x="0" y="5" width="50" height="30" rx="5" fill="#ef4444" opacity="0.3" stroke="#ef4444" stroke-width="2"/>
      <rect x="5" y="10" width="8" height="20" fill="#ef4444" opacity="0.6"/>
      <rect x="15" y="10" width="8" height="20" fill="#ef4444" opacity="0.8"/>
      <rect x="25" y="10" width="8" height="20" fill="#ef4444"/>
      <rect x="35" y="10" width="8" height="20" fill="#ef4444" opacity="0.8"/>
      <text x="25" y="60" text-anchor="middle" font-size="11" fill="#d1d5db">GPU/CPU</text>
    </g>
    
    <!-- Model icon -->
    <g transform="translate(105, 75)">
      <circle cx="25" cy="20" r="18" fill="#a78bfa" opacity="0.3"/>
      <circle cx="15" cy="15" r="6" fill="#a78bfa"/>
      <circle cx="35" cy="15" r="6" fill="#a78bfa"/>
      <circle cx="25" cy="28" r="6" fill="#a78bfa"/>
      <line x1="15" y1="15" x2="25" y2="28" stroke="#a78bfa" stroke-width="2"/>
      <line x1="35" y1="15" x2="25" y2="28" stroke="#a78bfa" stroke-width="2"/>
      <text x="25" y="60" text-anchor="middle" font-size="11" fill="#d1d5db">512x512</text>
    </g>
    
    <!-- Speed icon -->
    <g transform="translate(180, 75)">
      <path d="M 25 10 L 35 25 L 20 25 Z" fill="#fbbf24"/>
      <path d="M 20 25 L 30 35 L 15 35 Z" fill="#fbbf24" opacity="0.7"/>
      <text x="25" y="60" text-anchor="middle" font-size="11" fill="#d1d5db">1-step</text>
    </g>
  </g>
  
  <!-- Arrow back to Frontend -->
  <g>
    <path d="M 520 400 L 420 400 L 420 160 L 380 160" stroke="url(#archGrad2)" stroke-width="4" marker-end="url(#arrowGreen)" opacity="0.8">
      <animate attributeName="stroke-dasharray" values="0,800;800,0" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="stroke-dashoffset" values="0;-800" dur="3s" repeatCount="indefinite"/>
    </path>
    <text x="420" y="280" text-anchor="middle" font-size="12" font-weight="bold" fill="#10b981" transform="rotate(-90 420 280)">Styled Frames</text>
  </g>
  
  <!-- Ant Media Section -->
  <g transform="translate(100, 320)">
    <rect x="0" y="0" width="280" height="120" rx="15" fill="url(#archGrad2)" opacity="0.15" stroke="url(#archGrad2)" stroke-width="3" filter="url(#shadow)"/>
    <text x="140" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#10b981">ANT MEDIA SERVER</text>
    <text x="140" y="55" text-anchor="middle" font-size="13" fill="#9ca3af">WebRTC Broadcasting</text>
    
    <!-- Broadcast icon -->
    <g transform="translate(70, 70)">
      <circle cx="0" cy="0" r="20" fill="#10b981" opacity="0.2">
        <animate attributeName="r" values="20;30;20" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.2;0;0.2" dur="2s" repeatCount="indefinite"/>
      </circle>
      <circle cx="0" cy="0" r="12" fill="#10b981"/>
      <circle cx="0" cy="0" r="6" fill="#fff" opacity="0.9">
        <animate attributeName="opacity" values="0.9;0.4;0.9" dur="1s" repeatCount="indefinite"/>
      </circle>
    </g>
    
    <!-- Viewers icon -->
    <g transform="translate(150, 70)">
      <circle cx="-10" cy="0" r="10" fill="#3b82f6" opacity="0.8"/>
      <circle cx="5" cy="0" r="10" fill="#3b82f6" opacity="0.9"/>
      <circle cx="20" cy="0" r="10" fill="#3b82f6"/>
      <text x="5" y="30" text-anchor="middle" font-size="11" fill="#d1d5db">Viewers</text>
    </g>
  </g>
  
  <!-- Connection from Frontend to Ant Media -->
  <g>
    <path d="M 240 240 L 240 320" stroke="url(#archGrad2)" stroke-width="3" stroke-dasharray="5,5" marker-end="url(#arrowGreen)" opacity="0.6"/>
    <text x="260" y="280" text-anchor="start" font-size="11" fill="#10b981">Stream</text>
  </g>
  
  <!-- Performance metrics -->
  <g transform="translate(50, 490)">
    <text x="0" y="0" font-size="13" font-weight="bold" fill="#9ca3af">Performance:</text>
    <text x="0" y="20" font-size="11" fill="#10b981">GPU: 0.3-0.8s latency</text>
    <text x="200" y="20" font-size="11" fill="#f59e0b">CPU: 2-5s latency</text>
    <text x="400" y="20" font-size="11" fill="#3b82f6">Output: 1-3 FPS (GPU)</text>
    <text x="650" y="20" font-size="11" fill="#ef4444">Resolution: 512x512</text>
  </g>
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

## Use Cases

<div align="center">

<!-- Use Cases SVG -->
<svg width="850" height="280" viewBox="0 0 850 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="useGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="useGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ec4899;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#8b5cf6;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="useGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#10b981;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#059669;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="useGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ef4444;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#dc2626;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="useGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8b5cf6;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#6366f1;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="useGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f59e0b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#d97706;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Gaming Streams -->
  <g transform="translate(140, 70)">
    <circle cx="0" cy="0" r="50" fill="url(#useGrad1)" opacity="0.2"/>
    <circle cx="0" cy="0" r="40" fill="url(#useGrad1)" opacity="0.3"/>
    <rect x="-20" y="-15" width="40" height="30" rx="5" fill="url(#useGrad1)" opacity="0.8"/>
    <circle cx="-10" cy="-5" r="5" fill="#fff" opacity="0.9"/>
    <circle cx="10" cy="-5" r="5" fill="#fff" opacity="0.9"/>
    <rect x="-8" y="5" width="16" height="3" rx="1.5" fill="#fff" opacity="0.7"/>
    <rect x="-12" y="10" width="24" height="3" rx="1.5" fill="#fff" opacity="0.7"/>
    <text x="0" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#667eea">Gaming</text>
    <text x="0" y="92" text-anchor="middle" font-size="12" fill="#9ca3af">Streams</text>
  </g>
  
  <!-- Music Performances -->
  <g transform="translate(280, 70)">
    <circle cx="0" cy="0" r="50" fill="url(#useGrad2)" opacity="0.2"/>
    <circle cx="0" cy="0" r="40" fill="url(#useGrad2)" opacity="0.3"/>
    <circle cx="-8" cy="5" r="18" fill="url(#useGrad2)" opacity="0.8"/>
    <rect x="-10" y="-15" width="4" height="20" fill="url(#useGrad2)" opacity="0.8"/>
    <path d="M -10 -15 Q -5 -20 0 -15" fill="url(#useGrad2)" opacity="0.8"/>
    <path d="M 5 -10 Q 10 -5 15 0 Q 10 5 5 10 Q 0 5 -5 0 Q 0 -5 5 -10" fill="url(#useGrad2)" opacity="0.6"/>
    <line x1="12" y1="-8" x2="18" y2="-12" stroke="url(#useGrad2)" stroke-width="2"/>
    <line x1="12" y1="8" x2="18" y2="12" stroke="url(#useGrad2)" stroke-width="2"/>
    <text x="0" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#ec4899">Music</text>
    <text x="0" y="92" text-anchor="middle" font-size="12" fill="#9ca3af">Performances</text>
  </g>
  
  <!-- Live Events -->
  <g transform="translate(420, 70)">
    <circle cx="0" cy="0" r="50" fill="url(#useGrad3)" opacity="0.2"/>
    <circle cx="0" cy="0" r="40" fill="url(#useGrad3)" opacity="0.3"/>
    <path d="M -15 10 Q -15 -10 0 -20 Q 15 -10 15 10 L 10 10 Q 10 -5 0 -12 Q -10 -5 -10 10 Z" fill="url(#useGrad3)" opacity="0.8"/>
    <ellipse cx="0" cy="12" rx="18" ry="8" fill="url(#useGrad3)" opacity="0.6"/>
    <circle cx="-8" cy="-5" r="3" fill="#fff" opacity="0.9"/>
    <circle cx="8" cy="-5" r="3" fill="#fff" opacity="0.9"/>
    <path d="M -5 2 Q 0 5 5 2" stroke="#fff" stroke-width="2" fill="none" opacity="0.9"/>
    <text x="0" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#10b981">Live</text>
    <text x="0" y="92" text-anchor="middle" font-size="12" fill="#9ca3af">Events</text>
  </g>
  
  <!-- Live Shopping -->
  <g transform="translate(560, 70)">
    <circle cx="0" cy="0" r="50" fill="url(#useGrad4)" opacity="0.2"/>
    <circle cx="0" cy="0" r="40" fill="url(#useGrad4)" opacity="0.3"/>
    <rect x="-18" y="-8" width="36" height="24" rx="3" fill="url(#useGrad4)" opacity="0.8"/>
    <rect x="-15" y="-5" width="30" height="18" rx="2" fill="#1a1a2e"/>
    <path d="M -12 -15 L -8 -8 L 8 -8 L 12 -15 Z" fill="url(#useGrad4)" opacity="0.8"/>
    <circle cx="-8" cy="0" r="2" fill="#fbbf24"/>
    <circle cx="0" cy="0" r="2" fill="#fbbf24"/>
    <circle cx="8" cy="0" r="2" fill="#fbbf24"/>
    <path d="M -6 8 L -3 11 L 3 5" stroke="#10b981" stroke-width="2" fill="none"/>
    <text x="0" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#ef4444">Live</text>
    <text x="0" y="92" text-anchor="middle" font-size="12" fill="#9ca3af">Shopping</text>
  </g>
  
  <!-- Education Content -->
  <g transform="translate(700, 70)">
    <circle cx="0" cy="0" r="50" fill="url(#useGrad5)" opacity="0.2"/>
    <circle cx="0" cy="0" r="40" fill="url(#useGrad5)" opacity="0.3"/>
    <rect x="-15" y="-18" width="30" height="36" rx="3" fill="url(#useGrad5)" opacity="0.8"/>
    <rect x="-12" y="-15" width="24" height="30" rx="2" fill="#1a1a2e"/>
    <line x1="-8" y1="-10" x2="8" y2="-10" stroke="url(#useGrad5)" stroke-width="2"/>
    <line x1="-8" y1="-3" x2="8" y2="-3" stroke="url(#useGrad5)" stroke-width="2"/>
    <line x1="-8" y1="4" x2="8" y2="4" stroke="url(#useGrad5)" stroke-width="2"/>
    <line x1="-8" y1="11" x2="4" y2="11" stroke="url(#useGrad5)" stroke-width="2"/>
    <text x="0" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#8b5cf6">Education</text>
    <text x="0" y="92" text-anchor="middle" font-size="12" fill="#9ca3af">Content</text>
  </g>
  
  <!-- Art Streams -->
  <g transform="translate(140, 210)">
    <circle cx="0" cy="0" r="50" fill="url(#useGrad6)" opacity="0.2"/>
    <circle cx="0" cy="0" r="40" fill="url(#useGrad6)" opacity="0.3"/>
    <rect x="-18" y="-15" width="36" height="30" rx="4" fill="url(#useGrad6)" opacity="0.8"/>
    <rect x="-15" y="-12" width="30" height="24" rx="2" fill="#1a1a2e"/>
    <circle cx="-5" cy="-5" r="4" fill="#ec4899" opacity="0.7"/>
    <rect x="2" y="-8" width="8" height="8" fill="#10b981" opacity="0.7"/>
    <path d="M -8 5 L -3 10 L 2 5" fill="#fbbf24" opacity="0.7"/>
    <circle cx="8" cy="8" r="3" fill="#3b82f6" opacity="0.7"/>
    <path d="M -20 18 L -15 10 L -10 18" fill="url(#useGrad6)" opacity="0.6"/>
    <circle cx="-17" cy="20" r="2" fill="url(#useGrad6)"/>
    <text x="0" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#f59e0b">Art</text>
    <text x="0" y="92" text-anchor="middle" font-size="12" fill="#9ca3af">Streams</text>
  </g>
  
  <!-- Podcasts -->
  <g transform="translate(280, 210)">
    <circle cx="0" cy="0" r="50" fill="url(#useGrad1)" opacity="0.2"/>
    <circle cx="0" cy="0" r="40" fill="url(#useGrad1)" opacity="0.3"/>
    <ellipse cx="0" cy="-5" rx="10" ry="15" fill="url(#useGrad1)" opacity="0.8"/>
    <rect x="-3" y="10" width="6" height="8" rx="1" fill="url(#useGrad1)" opacity="0.8"/>
    <path d="M -15 5 Q -15 -8 -10 -8" stroke="url(#useGrad1)" stroke-width="3" fill="none" opacity="0.6">
      <animate attributeName="opacity" values="0.6;0.2;0.6" dur="1.5s" repeatCount="indefinite"/>
    </path>
    <path d="M 15 5 Q 15 -8 10 -8" stroke="url(#useGrad1)" stroke-width="3" fill="none" opacity="0.6">
      <animate attributeName="opacity" values="0.6;0.2;0.6" dur="1.5s" begin="0.3s" repeatCount="indefinite"/>
    </path>
    <path d="M -8 18 L 0 25 L 8 18" stroke="url(#useGrad1)" stroke-width="3" fill="none"/>
    <text x="0" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#667eea">Podcasts</text>
    <text x="0" y="92" text-anchor="middle" font-size="12" fill="#9ca3af">Visual</text>
  </g>
  
  <!-- Fitness -->
  <g transform="translate(420, 210)">
    <circle cx="0" cy="0" r="50" fill="url(#useGrad3)" opacity="0.2"/>
    <circle cx="0" cy="0" r="40" fill="url(#useGrad3)" opacity="0.3"/>
    <circle cx="0" cy="-12" r="8" fill="url(#useGrad3)" opacity="0.8"/>
    <path d="M -6 -4 L -6 8 L -10 12 L -8 14 L 0 8" fill="url(#useGrad3)" opacity="0.8"/>
    <path d="M 6 -4 L 6 8 L 10 12 L 8 14 L 0 8" fill="url(#useGrad3)" opacity="0.8"/>
    <path d="M -4 0 L 4 0" stroke="url(#useGrad3)" stroke-width="2"/>
    <circle cx="-12" cy="6" r="3" fill="#fbbf24">
      <animate attributeName="cy" values="6;3;6" dur="1s" repeatCount="indefinite"/>
    </circle>
    <circle cx="12" cy="6" r="3" fill="#fbbf24">
      <animate attributeName="cy" values="6;3;6" dur="1s" begin="0.5s" repeatCount="indefinite"/>
    </circle>
    <text x="0" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#10b981">Fitness</text>
    <text x="0" y="92" text-anchor="middle" font-size="12" fill="#9ca3af">Classes</text>
  </g>
  
  <!-- Virtual Meetings -->
  <g transform="translate(560, 210)">
    <circle cx="0" cy="0" r="50" fill="url(#useGrad5)" opacity="0.2"/>
    <circle cx="0" cy="0" r="40" fill="url(#useGrad5)" opacity="0.3"/>
    <rect x="-20" y="-15" width="40" height="28" rx="4" fill="url(#useGrad5)" opacity="0.8"/>
    <rect x="-17" y="-12" width="34" height="22" rx="2" fill="#1a1a2e"/>
    <circle cx="-8" cy="-6" r="5" fill="#3b82f6" opacity="0.7"/>
    <circle cx="8" cy="-6" r="5" fill="#ec4899" opacity="0.7"/>
    <circle cx="-8" cy="5" r="5" fill="#10b981" opacity="0.7"/>
    <circle cx="8" cy="5" r="5" fill="#f59e0b" opacity="0.7"/>
    <circle cx="0" cy="20" r="6" fill="url(#useGrad5)">
      <animate attributeName="opacity" values="1;0.5;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="0" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#8b5cf6">Virtual</text>
    <text x="0" y="92" text-anchor="middle" font-size="12" fill="#9ca3af">Meetings</text>
  </g>
  
  <!-- Cooking Shows -->
  <g transform="translate(700, 210)">
    <circle cx="0" cy="0" r="50" fill="url(#useGrad4)" opacity="0.2"/>
    <circle cx="0" cy="0" r="40" fill="url(#useGrad4)" opacity="0.3"/>
    <ellipse cx="0" cy="5" rx="18" ry="12" fill="url(#useGrad4)" opacity="0.8"/>
    <ellipse cx="0" cy="5" rx="14" ry="9" fill="#1a1a2e"/>
    <path d="M -20 5 Q -18 -5 -12 -8" stroke="url(#useGrad4)" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M 20 5 Q 18 -5 12 -8" stroke="url(#useGrad4)" stroke-width="3" fill="none" stroke-linecap="round"/>
    <circle cx="-5" cy="0" r="2" fill="#fbbf24" opacity="0.8">
      <animate attributeName="cy" values="0;-8;0" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0.2;0.8" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="5" cy="2" r="2" fill="#fbbf24" opacity="0.8">
      <animate attributeName="cy" values="2;-6;2" dur="2s" begin="0.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0.2;0.8" dur="2s" begin="0.5s" repeatCount="indefinite"/>
    </circle>
    <text x="0" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#ef4444">Cooking</text>
    <text x="0" y="92" text-anchor="middle" font-size="12" fill="#9ca3af">Shows</text>
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
