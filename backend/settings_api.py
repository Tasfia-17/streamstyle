"""
Settings API - Separate HTTP endpoint for controls
Based on GenDJ's settings_api.py pattern
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Global settings state
class Settings:
    def __init__(self):
        self.prompt = "artistic painting style"
        self.strength = 0.5
        self.guidance_scale = 0.0
        self.num_inference_steps = 1
        
settings = Settings()

class PromptRequest(BaseModel):
    prompt: str

class StrengthRequest(BaseModel):
    strength: float

class SettingsResponse(BaseModel):
    prompt: str
    strength: float
    guidance_scale: float
    num_inference_steps: int

@router.post("/prompt")
async def set_prompt(request: PromptRequest):
    """Update the AI prompt"""
    settings.prompt = request.prompt
    return {"status": "updated", "prompt": settings.prompt}

@router.post("/strength")
async def set_strength(request: StrengthRequest):
    """Update the transformation strength (0.0-1.0)"""
    settings.strength = max(0.0, min(1.0, request.strength))
    return {"status": "updated", "strength": settings.strength}

@router.get("/settings")
async def get_settings():
    """Get current settings"""
    return SettingsResponse(
        prompt=settings.prompt,
        strength=settings.strength,
        guidance_scale=settings.guidance_scale,
        num_inference_steps=settings.num_inference_steps
    )

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@router.get("/readyz")
async def readiness_check():
    """Readiness check for load balancers"""
    return {"status": "ready"}
