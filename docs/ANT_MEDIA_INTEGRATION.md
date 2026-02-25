# Ant Media Server Integration Guide

## Prerequisites

1. **Install Ant Media Server**
   - Download from: https://antmedia.io/
   - Or use Docker:
   ```bash
   docker run -d --name antmedia \
     -p 5080:5080 -p 1935:1935 \
     -p 5443:5443 \
     antmedia/antmediaserver:latest
   ```

2. **Access Dashboard**
   - Open: `http://localhost:5080`
   - Create application (e.g., "streamstyle")

## Frontend Integration

### 1. Install Ant Media WebRTC SDK

```bash
cd frontend
npm install @antmedia/webrtc_adaptor
```

### 2. Add to App.jsx

```javascript
import { WebRTCAdaptor } from '@antmedia/webrtc_adaptor'

// Add state
const [antMediaAdaptor, setAntMediaAdaptor] = useState(null)
const [isPublishing, setIsPublishing] = useState(false)

// Initialize Ant Media
const initAntMedia = () => {
  const adaptor = new WebRTCAdaptor({
    websocket_url: 'ws://localhost:5080/WebRTCAppEE/websocket',
    mediaConstraints: {
      video: false, // We'll provide canvas stream
      audio: false
    },
    peerconnection_config: {
      iceServers: [{ urls: 'stun:stun.l.google.com:19302' }]
    },
    sdp_constraints: {
      OfferToReceiveAudio: false,
      OfferToReceiveVideo: false
    },
    localVideoId: 'localVideo',
    callback: (info, obj) => {
      if (info === 'initialized') {
        console.log('✅ Ant Media initialized')
      } else if (info === 'publish_started') {
        console.log('📡 Publishing started')
        setIsPublishing(true)
      } else if (info === 'publish_finished') {
        console.log('📡 Publishing stopped')
        setIsPublishing(false)
      }
    },
    callbackError: (error) => {
      console.error('❌ Ant Media error:', error)
    }
  })
  
  setAntMediaAdaptor(adaptor)
}

// Start publishing styled stream
const startAntMediaPublish = () => {
  if (!antMediaAdaptor) {
    initAntMedia()
    return
  }
  
  // Create canvas stream from styled output
  const canvas = document.createElement('canvas')
  canvas.width = 640
  canvas.height = 480
  const ctx = canvas.getContext('2d')
  
  // Draw styled image to canvas continuously
  const drawInterval = setInterval(() => {
    if (styledImage) {
      const img = new Image()
      img.onload = () => {
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height)
      }
      img.src = styledImage
    }
  }, 100)
  
  // Get stream from canvas
  const stream = canvas.captureStream(10) // 10 FPS
  
  // Publish to Ant Media
  const streamId = 'streamstyle-' + Date.now()
  antMediaAdaptor.publish(streamId, null, null, stream)
  
  console.log('📡 Publishing to Ant Media:', streamId)
}

// Stop publishing
const stopAntMediaPublish = () => {
  if (antMediaAdaptor) {
    antMediaAdaptor.stop()
  }
}
```

### 3. Add UI Button

```jsx
{isStreaming && (
  <button 
    className={isPublishing ? "publish-btn active" : "publish-btn"}
    onClick={isPublishing ? stopAntMediaPublish : startAntMediaPublish}
  >
    {isPublishing ? '📡 Broadcasting' : '📡 Broadcast to Viewers'}
  </button>
)}
```

## Viewer Page

Create `frontend/src/Viewer.jsx`:

```javascript
import { useEffect, useRef } from 'react'
import { WebRTCAdaptor } from '@antmedia/webrtc_adaptor'

function Viewer() {
  const videoRef = useRef(null)
  
  useEffect(() => {
    const adaptor = new WebRTCAdaptor({
      websocket_url: 'ws://localhost:5080/WebRTCAppEE/websocket',
      mediaConstraints: {
        video: false,
        audio: false
      },
      remoteVideoId: 'remoteVideo',
      callback: (info) => {
        if (info === 'play_started') {
          console.log('▶️ Playback started')
        }
      }
    })
    
    // Play stream (replace with actual stream ID)
    const streamId = 'streamstyle-1234567890'
    adaptor.play(streamId)
    
    return () => adaptor.stop()
  }, [])
  
  return (
    <div className="viewer">
      <h1>🎨 StreamStyle AI - Live View</h1>
      <video id="remoteVideo" ref={videoRef} autoPlay playsInline />
    </div>
  )
}

export default Viewer
```

## Testing

1. **Start Ant Media Server**
   ```bash
   docker start antmedia
   ```

2. **Start StreamStyle AI**
   ```bash
   ./start.sh
   ```

3. **Publish Stream**
   - Click "Start Streaming"
   - Wait for styled output
   - Click "Broadcast to Viewers"

4. **View Stream**
   - Open viewer page
   - Or use Ant Media dashboard player

## Production Deployment

### Environment Variables

```bash
# .env
VITE_ANT_MEDIA_URL=wss://your-domain.com:5443/WebRTCAppEE/websocket
VITE_BACKEND_URL=wss://your-domain.com/ws
```

### HTTPS Required

Ant Media requires HTTPS in production:

```bash
# Use Let's Encrypt
sudo ./enable_ssl.sh -d your-domain.com
```

## Architecture with Ant Media

```
User Browser
    ↓ Webcam
StreamStyle Frontend
    ↓ WebSocket
StreamStyle Backend (AI Processing)
    ↓ Styled Frames
Frontend Canvas
    ↓ Canvas Stream
Ant Media Server (WebRTC)
    ↓ Broadcast
Multiple Viewers (WebRTC)
```

## Performance Notes

- **Latency**: 0.5-2 seconds for viewers
- **Scalability**: 100+ concurrent viewers per stream
- **Bandwidth**: ~1-3 Mbps per viewer
- **Canvas FPS**: 10 FPS (balance quality/performance)

## Troubleshooting

**Connection refused:**
- Check Ant Media is running: `docker ps`
- Verify port 5080 is accessible

**No video in viewer:**
- Check stream ID matches
- Verify WebRTC ports (1935, 5443) are open

**High latency:**
- Reduce canvas stream FPS
- Use lower resolution
- Check network bandwidth
