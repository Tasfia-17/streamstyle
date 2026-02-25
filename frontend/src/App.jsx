import { useState, useRef, useEffect } from 'react'
import './App.css'

const WS_URL = 'ws://localhost:8000/ws'

const STYLE_PRESETS = [
  { name: 'Oil Painting', prompt: 'oil painting, artistic style' },
  { name: 'Cyberpunk', prompt: 'cyberpunk neon style, futuristic' },
  { name: 'Anime', prompt: 'anime style art, manga' },
  { name: 'Watercolor', prompt: 'watercolor painting, soft colors' },
  { name: 'Pixel Art', prompt: 'pixel art, 8-bit retro style' },
  { name: 'Van Gogh', prompt: 'van gogh style, impressionist painting' },
  { name: 'Sketch', prompt: 'pencil sketch drawing, black and white' },
  { name: 'Pop Art', prompt: 'pop art style, bold colors, comic book' }
]

function App() {
  const [prompt, setPrompt] = useState('artistic painting style')
  const [isStreaming, setIsStreaming] = useState(false)
  const [status, setStatus] = useState('Disconnected')
  const [styledImage, setStyledImage] = useState(null)
  const [voiceEnabled, setVoiceEnabled] = useState(false)
  const [fps, setFps] = useState(0)
  
  const videoRef = useRef(null)
  const canvasRef = useRef(null)
  const wsRef = useRef(null)
  const streamIntervalRef = useRef(null)
  const recognitionRef = useRef(null)
  const frameCountRef = useRef(0)
  const fpsIntervalRef = useRef(null)

  useEffect(() => {
    return () => {
      stopStreaming()
      stopVoiceControl()
    }
  }, [])

  const connectWebSocket = () => {
    const ws = new WebSocket(WS_URL)
    
    ws.onopen = () => {
      setStatus('Connected')
      console.log('✅ WebSocket connected')
    }
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data)
      
      if (data.type === 'styled_frame') {
        setStyledImage(data.image)
        frameCountRef.current++
      } else if (data.type === 'prompt_updated') {
        console.log('🎨 Prompt updated:', data.prompt)
      }
    }
    
    ws.onerror = (error) => {
      console.error('❌ WebSocket error:', error)
      setStatus('Error')
    }
    
    ws.onclose = () => {
      setStatus('Disconnected')
      console.log('🔌 WebSocket disconnected')
    }
    
    wsRef.current = ws
  }

  const startStreaming = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ 
        video: { width: 640, height: 480 } 
      })
      
      videoRef.current.srcObject = stream
      await videoRef.current.play()
      
      connectWebSocket()
      setIsStreaming(true)
      setStatus('Streaming')
      
      // Send frames every 200ms (5 FPS)
      streamIntervalRef.current = setInterval(() => {
        if (wsRef.current?.readyState === WebSocket.OPEN) {
          captureAndSendFrame()
        }
      }, 200)
      
      // FPS counter
      frameCountRef.current = 0
      fpsIntervalRef.current = setInterval(() => {
        setFps(frameCountRef.current)
        frameCountRef.current = 0
      }, 1000)
      
    } catch (err) {
      console.error('❌ Error accessing webcam:', err)
      setStatus('Camera Error')
    }
  }

  const stopStreaming = () => {
    if (streamIntervalRef.current) {
      clearInterval(streamIntervalRef.current)
    }
    
    if (fpsIntervalRef.current) {
      clearInterval(fpsIntervalRef.current)
    }
    
    if (videoRef.current?.srcObject) {
      videoRef.current.srcObject.getTracks().forEach(track => track.stop())
    }
    
    if (wsRef.current) {
      wsRef.current.close()
    }
    
    setIsStreaming(false)
    setStatus('Disconnected')
    setStyledImage(null)
    setFps(0)
  }

  const captureAndSendFrame = () => {
    const canvas = canvasRef.current
    const video = videoRef.current
    
    if (!canvas || !video) return
    
    canvas.width = video.videoWidth
    canvas.height = video.videoHeight
    
    const ctx = canvas.getContext('2d')
    ctx.drawImage(video, 0, 0)
    
    const imageData = canvas.toDataURL('image/jpeg', 0.8)
    
    wsRef.current.send(JSON.stringify({
      type: 'frame',
      image: imageData
    }))
  }

  const updatePrompt = (newPrompt) => {
    setPrompt(newPrompt)
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({
        type: 'prompt',
        prompt: newPrompt
      }))
    }
  }

  const applyPreset = (preset) => {
    updatePrompt(preset.prompt)
  }

  const startVoiceControl = () => {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
      alert('Voice recognition not supported in this browser')
      return
    }

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    const recognition = new SpeechRecognition()
    
    recognition.continuous = true
    recognition.interimResults = false
    recognition.lang = 'en-US'
    
    recognition.onresult = (event) => {
      const transcript = event.results[event.results.length - 1][0].transcript.toLowerCase()
      console.log('🎤 Heard:', transcript)
      
      // Match voice commands to presets
      STYLE_PRESETS.forEach(preset => {
        if (transcript.includes(preset.name.toLowerCase())) {
          console.log('🎨 Applying:', preset.name)
          applyPreset(preset)
        }
      })
    }
    
    recognition.onerror = (event) => {
      console.error('🎤 Voice error:', event.error)
    }
    
    recognition.start()
    recognitionRef.current = recognition
    setVoiceEnabled(true)
    console.log('🎤 Voice control started')
  }

  const stopVoiceControl = () => {
    if (recognitionRef.current) {
      recognitionRef.current.stop()
      recognitionRef.current = null
      setVoiceEnabled(false)
      console.log('🎤 Voice control stopped')
    }
  }

  return (
    <div className="app">
      <header>
        <h1>🎨 StreamStyle AI</h1>
        <p>Real-Time AI Video Styling</p>
      </header>

      <div className="controls">
        <div className="prompt-section">
          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Enter style prompt..."
            disabled={!isStreaming}
          />
          <button onClick={() => updatePrompt(prompt)} disabled={!isStreaming}>
            Apply Style
          </button>
        </div>
        
        <div className="presets">
          {STYLE_PRESETS.map((preset) => (
            <button
              key={preset.name}
              className="preset-btn"
              onClick={() => applyPreset(preset)}
              disabled={!isStreaming}
            >
              {preset.name}
            </button>
          ))}
        </div>
        
        <div className="stream-controls">
          {!isStreaming ? (
            <button className="start-btn" onClick={startStreaming}>
              🎥 Start Streaming
            </button>
          ) : (
            <button className="stop-btn" onClick={stopStreaming}>
              ⏹ Stop Streaming
            </button>
          )}
          
          {isStreaming && (
            voiceEnabled ? (
              <button className="voice-btn active" onClick={stopVoiceControl}>
                🎤 Voice ON
              </button>
            ) : (
              <button className="voice-btn" onClick={startVoiceControl}>
                🎤 Voice Control
              </button>
            )
          )}
          
          <span className={`status ${status.toLowerCase()}`}>
            {status}
          </span>
          
          {isStreaming && (
            <span className="fps">
              {fps} FPS
            </span>
          )}
        </div>
      </div>

      <div className="video-container">
        <div className="video-box">
          <h3>Original</h3>
          <video ref={videoRef} autoPlay playsInline muted />
        </div>
        
        <div className="video-box">
          <h3>Styled Output</h3>
          {styledImage ? (
            <img src={styledImage} alt="Styled output" />
          ) : (
            <div className="placeholder">
              {isStreaming ? 'Processing...' : 'Start streaming to see styled output'}
            </div>
          )}
        </div>
      </div>

      <canvas ref={canvasRef} style={{ display: 'none' }} />
    </div>
  )
}

export default App
