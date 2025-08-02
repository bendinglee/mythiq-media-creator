from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import json
from datetime import datetime
import logging
import base64
import io

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configuration
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
HUGGINGFACE_API_KEY = os.environ.get('HUGGINGFACE_API_KEY')

class MediaCreator:
    def __init__(self):
        self.groq_available = bool(GROQ_API_KEY)
        self.hf_available = bool(HUGGINGFACE_API_KEY)
        
    def enhance_prompt_with_ai(self, prompt, media_type):
        """Use Groq to enhance and optimize prompts for better media generation"""
        if not self.groq_available:
            return prompt
            
        try:
            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }
            
            system_prompt = f"""You are an expert {media_type} prompt engineer. Enhance the user's prompt to create better {media_type} generation results.

For images: Add artistic style, lighting, composition, and quality descriptors.
For videos: Add camera movement, scene dynamics, and visual effects.
For audio: Add mood, instruments, tempo, and audio characteristics.

Return only the enhanced prompt, nothing else."""
            
            data = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Enhance this {media_type} prompt: {prompt}"}
                ],
                "model": "llama-3.1-70b-versatile",
                "temperature": 0.7,
                "max_tokens": 200
            }
            
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                enhanced = result['choices'][0]['message']['content'].strip()
                return enhanced if enhanced else prompt
            else:
                logger.error(f"Groq API error: {response.status_code}")
                return prompt
                
        except Exception as e:
            logger.error(f"Prompt enhancement error: {str(e)}")
            return prompt
    
    def generate_image_hf(self, prompt):
        """Generate image using HuggingFace Stable Diffusion"""
        if not self.hf_available:
            return None
            
        try:
            headers = {
                "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
                "Content-Type": "application/json"
            }
            
            # Try multiple models for better results
            models = [
                "stabilityai/stable-diffusion-xl-base-1.0",
                "runwayml/stable-diffusion-v1-5",
                "CompVis/stable-diffusion-v1-4"
            ]
            
            for model in models:
                try:
                    data = {
                        "inputs": prompt,
                        "parameters": {
                            "num_inference_steps": 20,
                            "guidance_scale": 7.5,
                            "width": 512,
                            "height": 512
                        }
                    }
                    
                    response = requests.post(
                        f"https://api-inference.huggingface.co/models/{model}",
                        headers=headers,
                        json=data,
                        timeout=60
                    )
                    
                    if response.status_code == 200:
                        # Convert image to base64
                        image_bytes = response.content
                        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
                        return f"data:image/png;base64,{image_base64}"
                    
                except Exception as model_error:
                    logger.warning(f"Model {model} failed: {str(model_error)}")
                    continue
            
            return None
            
        except Exception as e:
            logger.error(f"HuggingFace image generation error: {str(e)}")
            return None
    
    def generate_placeholder_image(self, prompt):
        """Generate placeholder image when AI is unavailable"""
        try:
            # Use placeholder service with custom text
            width, height = 512, 512
            text = prompt[:50] + "..." if len(prompt) > 50 else prompt
            
            # Create a simple colored placeholder
            placeholder_url = f"https://via.placeholder.com/{width}x{height}/6366f1/ffffff?text={text.replace(' ', '+')}"
            
            response = requests.get(placeholder_url, timeout=10)
            if response.status_code == 200:
                image_base64 = base64.b64encode(response.content).decode('utf-8')
                return f"data:image/png;base64,{image_base64}"
            
            return None
            
        except Exception as e:
            logger.error(f"Placeholder generation error: {str(e)}")
            return None
    
    def generate_video_concept(self, prompt):
        """Generate video concept and storyboard"""
        enhanced_prompt = self.enhance_prompt_with_ai(prompt, "video")
        
        # For now, return a detailed concept since video generation requires heavy resources
        return {
            "concept": enhanced_prompt,
            "storyboard": [
                {"scene": 1, "description": f"Opening scene: {enhanced_prompt[:100]}"},
                {"scene": 2, "description": "Main action sequence with dynamic movement"},
                {"scene": 3, "description": "Climactic moment with visual effects"},
                {"scene": 4, "description": "Resolution and closing scene"}
            ],
            "technical_specs": {
                "duration": "10-15 seconds",
                "resolution": "1920x1080",
                "frame_rate": "30fps",
                "style": "Cinematic with smooth transitions"
            },
            "note": "Video generation requires specialized GPU resources. This concept can be used with video generation tools like RunwayML or Stable Video Diffusion."
        }
    
    def generate_audio_concept(self, prompt):
        """Generate audio concept and composition"""
        enhanced_prompt = self.enhance_prompt_with_ai(prompt, "audio")
        
        return {
            "concept": enhanced_prompt,
            "composition": {
                "intro": "Atmospheric opening (0-5s)",
                "main": "Core melody and rhythm (5-25s)",
                "bridge": "Transition or variation (25-35s)",
                "outro": "Fade out or conclusion (35-40s)"
            },
            "technical_specs": {
                "duration": "30-60 seconds",
                "format": "WAV/MP3",
                "sample_rate": "44.1kHz",
                "quality": "High fidelity"
            },
            "instruments": ["Synthesizer", "Digital drums", "Ambient pads", "Bass"],
            "note": "Audio generation requires specialized models. This concept can be used with tools like MusicGen or AudioCraft."
        }

# Initialize media creator
media_creator = MediaCreator()

@app.route('/')
def home():
    """Service status endpoint"""
    return jsonify({
        "service": "Mythiq Media Creator",
        "status": "online",
        "version": "2.0.0",
        "message": "AI-powered media generation with HuggingFace integration",
        "features": [
            "AI image generation with Stable Diffusion",
            "Prompt enhancement with Groq",
            "Video concept generation",
            "Audio composition planning",
            "Multiple fallback options"
        ],
        "ai_status": {
            "groq_available": media_creator.groq_available,
            "huggingface_available": media_creator.hf_available
        },
        "endpoints": ["/generate-image", "/generate-video", "/generate-audio", "/health"],
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "service": "mythiq-media-creator",
        "status": "healthy",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/generate-image', methods=['POST'])
def generate_image():
    """Generate image from text prompt"""
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({"error": "Image prompt is required"}), 400
        
        prompt = data['prompt'].strip()
        if not prompt:
            return jsonify({"error": "Image prompt cannot be empty"}), 400
        
        # Enhance prompt with AI
        enhanced_prompt = media_creator.enhance_prompt_with_ai(prompt, "image")
        
        # Try to generate with HuggingFace
        image_data = media_creator.generate_image_hf(enhanced_prompt)
        
        if image_data:
            return jsonify({
                "image": image_data,
                "original_prompt": prompt,
                "enhanced_prompt": enhanced_prompt,
                "provider": "huggingface",
                "timestamp": datetime.now().isoformat()
            })
        else:
            # Fallback to placeholder
            placeholder = media_creator.generate_placeholder_image(prompt)
            return jsonify({
                "image": placeholder,
                "original_prompt": prompt,
                "enhanced_prompt": enhanced_prompt,
                "provider": "placeholder",
                "note": "AI image generation temporarily unavailable, showing placeholder",
                "timestamp": datetime.now().isoformat()
            })
        
    except Exception as e:
        logger.error(f"Image generation error: {str(e)}")
        return jsonify({"error": "Could not generate image"}), 500

@app.route('/generate-video', methods=['POST'])
def generate_video():
    """Generate video concept from text prompt"""
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({"error": "Video prompt is required"}), 400
        
        prompt = data['prompt'].strip()
        if not prompt:
            return jsonify({"error": "Video prompt cannot be empty"}), 400
        
        # Generate video concept
        video_concept = media_creator.generate_video_concept(prompt)
        
        return jsonify({
            "video_concept": video_concept,
            "original_prompt": prompt,
            "provider": "groq" if media_creator.groq_available else "template",
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Video generation error: {str(e)}")
        return jsonify({"error": "Could not generate video concept"}), 500

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    """Generate audio concept from text prompt"""
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({"error": "Audio prompt is required"}), 400
        
        prompt = data['prompt'].strip()
        if not prompt:
            return jsonify({"error": "Audio prompt cannot be empty"}), 400
        
        # Generate audio concept
        audio_concept = media_creator.generate_audio_concept(prompt)
        
        return jsonify({
            "audio_concept": audio_concept,
            "original_prompt": prompt,
            "provider": "groq" if media_creator.groq_available else "template",
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Audio generation error: {str(e)}")
        return jsonify({"error": "Could not generate audio concept"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    logger.info(f"Starting Mythiq Media Creator on port {port}")
    logger.info(f"Groq API available: {media_creator.groq_available}")
    logger.info(f"HuggingFace API available: {media_creator.hf_available}")
    
    app.run(host='0.0.0.0', port=port, debug=False)
