# StreamStyle AI - Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         FRONTEND                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │   Webcam     │───▶│ Frame Queue  │───▶│  WebSocket   │  │
│  │  640x480     │    │  (200ms)     │    │   Client     │  │
│  └──────────────┘    └──────────────┘    └──────┬───────┘  │
│                                                   │          │
│  ┌──────────────┐    ┌──────────────┐           │          │
│  │ Styled Video │◀───│ Canvas Draw  │◀──────────┘          │
│  │   Display    │    │              │                       │
│  └──────────────┘    └──────┬───────┘                       │
│                              │                               │
│                              ▼                               │
│                      ┌──────────────┐                        │
│                      │ Ant Media    │                        │
│                      │ WebRTC Pub   │                        │
│                      └──────────────┘                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ WebSocket
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                         BACKEND                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │  WebSocket   │───▶│ Frame Queue  │───▶│   Async      │  │
│  │   Server     │    │  (FIFO)      │    │  Processor   │  │
│  └──────────────┘    └──────────────┘    └──────┬───────┘  │
│                                                   │          │
│                                                   ▼          │
│                                          ┌──────────────┐   │
│                                          │  SD Turbo    │   │
│                                          │  512x512     │   │
│                                          │  1-step      │   │
│                                          │  float16     │   │
│                                          └──────┬───────┘   │
│                                                 │           │
│  ┌──────────────┐                              │           │
│  │  Response    │◀─────────────────────────────┘           │
│  │  (base64)    │                                           │
│  └──────────────┘                                           │
└─────────────────────────────────────────────────────────────┘
```

## Component Responsibilities

### Frontend
- **Webcam Capture**: 640x480 @ 30fps native
- **Frame Sampling**: Extract 1 frame every 200ms (5 FPS)
- **WebSocket Client**: Send frames, receive styled results
- **Canvas Rendering**: Display styled output
- **Ant Media Publisher**: Broadcast styled stream to viewers
- **UI Controls**: Prompt input, voice commands, presets

### Backend
- **WebSocket Server**: Handle concurrent connections
- **Frame Queue**: FIFO with max size (prevent backlog)
- **AI Processing**: Async SD Turbo inference
- **Model Management**: Preload, GPU optimization
- **Response Streaming**: Return styled frames immediately

### AI Optimization Strategy
1. **Model**: Stable Diffusion Turbo (1-step)
2. **Precision**: float16 (half precision)
3. **Resolution**: 512x512 (downscale input)
4. **Batch Size**: 1 (real-time priority)
5. **Compilation**: torch.compile for 20-30% speedup
6. **Caching**: Keep model in GPU memory

### Streaming Integration (Ant Media)
- Capture styled canvas as MediaStream
- Use Ant Media WebRTC SDK
- Publish to Ant Media Server
- Viewers watch via WebRTC player
- Sub-second latency for viewers

### Latency Mitigation
| Component | Target | Strategy |
|-----------|--------|----------|
| Frame Capture | <10ms | Native browser API |
| Network Send | <50ms | WebSocket, local network |
| AI Processing | <500ms | GPU, float16, 512x512 |
| Network Return | <50ms | WebSocket |
| Render | <16ms | Canvas 2D |
| **Total** | **<650ms** | **Acceptable for demo** |

## Performance Targets

- **Processing**: 5 FPS (200ms intervals)
- **Latency**: <1 second end-to-end
- **GPU Memory**: <4GB
- **CPU Usage**: <50% (when GPU available)
- **Network**: <1 Mbps per client

## Scalability Notes

- Single backend handles 1-5 concurrent users
- Ant Media handles 100+ viewers per stream
- For production: Add Redis queue, multiple workers
