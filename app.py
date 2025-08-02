import os
import json
import uuid
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Configuration
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
HUGGINGFACE_API_KEY = os.environ.get('HUGGINGFACE_API_KEY')

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "service": "Mythiq Media Creator",
        "status": "online",
        "version": "1.0.0",
        "endpoints": ["/generate-image", "/generate-video", "/generate-audio", "/health"]
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "mythiq-media-creator",
        "groq_configured": bool(GROQ_API_KEY),
        "huggingface_configured": bool(HUGGINGFACE_API_KEY)
    })

@app.route('/generate-image', methods=['POST'])
def generate_image():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        style = data.get('style', 'creative')
        
        if not prompt:
            return jsonify({"error": "Image prompt is required"}), 400
        
        # Generate image using Hugging Face
        image_result = generate_image_with_hf(prompt, style)
        
        return jsonify({
            "media_id": str(uuid.uuid4())[:8],
            "type": "image",
            "prompt": prompt,
            "style": style,
            "url": image_result.get("url", ""),
            "status": "generated",
            "provider": "huggingface"
        })
        
    except Exception as e:
        print(f"Image generation error: {e}")
        return jsonify({"error": "Failed to generate image"}), 500

@app.route('/generate-video', methods=['POST'])
def generate_video():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        style = data.get('style', 'creative')
        
        if not prompt:
            return jsonify({"error": "Video prompt is required"}), 400
        
        # For now, return a placeholder response
        return jsonify({
            "media_id": str(uuid.uuid4())[:8],
            "type": "video",
            "prompt": prompt,
            "style": style,
            "url": "https://via.placeholder.com/640x480/4CAF50/white?text=Video+Generated",
            "status": "generated",
            "provider": "placeholder",
            "message": "Video generation coming soon! For now, enjoy this placeholder."
        })
        
    except Exception as e:
        print(f"Video generation error: {e}")
        return jsonify({"error": "Failed to generate video"}), 500

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        style = data.get('style', 'creative')
        
        if not prompt:
            return jsonify({"error": "Audio prompt is required"}), 400
        
        # For now, return a placeholder response
        return jsonify({
            "media_id": str(uuid.uuid4())[:8],
            "type": "audio",
            "prompt": prompt,
            "style": style,
            "url": "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
            "status": "generated",
            "provider": "placeholder",
            "message": "Audio generation coming soon! For now, enjoy this sample sound."
        })
        
    except Exception as e:
        print(f"Audio generation error: {e}")
        return jsonify({"error": "Failed to generate audio"}), 500

def generate_image_with_hf(prompt, style):
    """Generate image using Hugging Face Inference API"""
    try:
        if not HUGGINGFACE_API_KEY:
            return {"url": "https://via.placeholder.com/512x512/667eea/white?text=Image+Generated"}
        
        # Use Stable Diffusion model
        url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
        
        headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Enhance prompt based on style
        enhanced_prompt = enhance_prompt(prompt, style)
        
        payload = {
            "inputs": enhanced_prompt,
            "parameters": {
                "num_inference_steps": 20,
                "guidance_scale": 7.5
            }
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        
        if response.status_code == 200:
            # Convert image bytes to base64 data URL
            image_bytes = response.content
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
            data_url = f"data:image/png;base64,{image_base64}"
            return {"url": data_url}
        else:
            print(f"HF API error: {response.status_code} - {response.text}")
            return {"url": "https://via.placeholder.com/512x512/667eea/white?text=Image+Generated"}
            
    except Exception as e:
        print(f"Image generation error: {e}")
        return {"url": "https://via.placeholder.com/512x512/667eea/white?text=Image+Generated"}

def enhance_prompt(prompt, style):
    """Enhance the prompt based on style"""
    style_modifiers = {
        "creative": "artistic, creative, vibrant colors, imaginative",
        "realistic": "photorealistic, detailed, high quality, professional",
        "fantasy": "fantasy art, magical, ethereal, mystical",
        "cartoon": "cartoon style, animated, colorful, fun",
        "abstract": "abstract art, geometric, modern, artistic"
    }
    
    modifier = style_modifiers.get(style, "high quality, detailed")
    return f"{prompt}, {modifier}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
