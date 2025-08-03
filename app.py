from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from datetime import datetime
import requests
import base64
import io

app = Flask(__name__)

# Enable CORS for your frontend domain
CORS(app, origins=[
    'https://mythiq-ui-production.up.railway.app',
    'http://localhost:5173',
    'http://localhost:3000'
])

# Configuration
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
HUGGINGFACE_API_KEY = os.environ.get('HUGGINGFACE_API_KEY')
MEDIA_OUTPUT_PATH = os.environ.get('MEDIA_OUTPUT_PATH', '/tmp/media')

def check_groq_availability():
    """Check if Groq API is available"""
    try:
        if not GROQ_API_KEY:
            return False
        
        headers = {
            'Authorization': f'Bearer {GROQ_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers=headers,
            json={
                'model': 'llama3-70b-8192',
                'messages': [{'role': 'user', 'content': 'test'}],
                'max_tokens': 1
            },
            timeout=5
        )
        return response.status_code == 200
    except:
        return False

def check_huggingface_availability():
    """Check if HuggingFace API is available"""
    try:
        if not HUGGINGFACE_API_KEY:
            return False
        
        headers = {'Authorization': f'Bearer {HUGGINGFACE_API_KEY}'}
        response = requests.get(
            'https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1',
            headers=headers,
            timeout=5
        )
        return response.status_code in [200, 503]  # 503 means model is loading
    except:
        return False

def enhance_prompt_with_groq(prompt):
    """Enhance image prompt using Groq"""
    try:
        if not GROQ_API_KEY:
            return prompt
        
        headers = {
            'Authorization': f'Bearer {GROQ_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        system_prompt = """You are an expert at writing detailed image generation prompts. 
        Take the user's simple prompt and enhance it with artistic details, style, lighting, and composition.
        Keep it under 200 words and focus on visual elements.
        Return only the enhanced prompt, no explanations."""
        
        response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers=headers,
            json={
                'model': 'llama3-70b-8192',
                'messages': [
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': f"Enhance this image prompt: {prompt}"}
                ],
                'max_tokens': 200,
                'temperature': 0.8
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            enhanced_prompt = data['choices'][0]['message']['content'].strip()
            return enhanced_prompt
        
    except Exception as e:
        print(f"Groq prompt enhancement error: {e}")
    
    return prompt

def generate_image_with_huggingface(prompt):
    """Generate image using HuggingFace Stable Diffusion"""
    try:
        if not HUGGINGFACE_API_KEY:
            return None
        
        headers = {'Authorization': f'Bearer {HUGGINGFACE_API_KEY}'}
        
        # Try Stable Diffusion 2.1
        response = requests.post(
            'https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1',
            headers=headers,
            json={'inputs': prompt},
            timeout=60
        )
        
        if response.status_code == 200:
            return response.content
        
        # Fallback to other models
        models = [
            'runwayml/stable-diffusion-v1-5',
            'CompVis/stable-diffusion-v1-4'
        ]
        
        for model in models:
            try:
                response = requests.post(
                    f'https://api-inference.huggingface.co/models/{model}',
                    headers=headers,
                    json={'inputs': prompt},
                    timeout=60
                )
                
                if response.status_code == 200:
                    return response.content
            except:
                continue
        
    except Exception as e:
        print(f"HuggingFace image generation error: {e}")
    
    return None

def generate_fallback_image():
    """Generate a simple fallback image as base64"""
    # Create a simple colored rectangle as fallback
    fallback_svg = """<svg width="512" height="512" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
            </linearGradient>
        </defs>
        <rect width="512" height="512" fill="url(#grad1)" />
        <text x="256" y="256" font-family="Arial, sans-serif" font-size="24" fill="white" text-anchor="middle" dominant-baseline="middle">
            🎨 AI Image
        </text>
        <text x="256" y="300" font-family="Arial, sans-serif" font-size="16" fill="white" text-anchor="middle" dominant-baseline="middle">
            Generated by Mythiq
        </text>
    </svg>"""
    
    return base64.b64encode(fallback_svg.encode()).decode()

@app.route('/', methods=['GET'])
def home():
    """Health check and service info"""
    groq_available = check_groq_availability()
    huggingface_available = check_huggingface_availability()
    
    return jsonify({
        'service': 'Mythiq Media Creator',
        'status': 'online',
        'version': '2.0.0',
        'timestamp': datetime.now().isoformat(),
        'ai_status': {
            'groq_available': groq_available,
            'huggingface_available': huggingface_available
        },
        'endpoints': [
            '/generate-image',
            '/generate-video',
            '/generate-audio',
            '/health'
        ],
        'features': [
            'AI image generation with Stable Diffusion',
            'Prompt enhancement with Groq',
            'Video concept generation',
            'Audio composition planning',
            'Multiple fallback options'
        ],
        'message': 'AI-powered media generation with HuggingFace integration'
    })

@app.route('/generate-image', methods=['POST', 'OPTIONS'])
def generate_image():
    """Generate an image based on user prompt"""
    
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({'error': 'Image prompt is required'}), 400
        
        original_prompt = data['prompt']
        
        # Enhance prompt with Groq if available
        enhanced_prompt = enhance_prompt_with_groq(original_prompt)
        
        # Generate image with HuggingFace
        image_data = generate_image_with_huggingface(enhanced_prompt)
        
        if image_data:
            # Convert to base64
            image_base64 = base64.b64encode(image_data).decode()
            
            return jsonify({
                'image_data': f'data:image/png;base64,{image_base64}',
                'original_prompt': original_prompt,
                'enhanced_prompt': enhanced_prompt,
                'source': 'huggingface',
                'model': 'stable-diffusion-2-1',
                'timestamp': datetime.now().isoformat(),
                'message': 'Image generated successfully'
            })
        
        # Fallback response
        fallback_image = generate_fallback_image()
        
        return jsonify({
            'image_data': f'data:image/svg+xml;base64,{fallback_image}',
            'original_prompt': original_prompt,
            'enhanced_prompt': enhanced_prompt,
            'source': 'fallback',
            'model': 'svg-generator',
            'timestamp': datetime.now().isoformat(),
            'message': 'Fallback image generated (AI services unavailable)'
        })
        
    except Exception as e:
        # Emergency fallback
        fallback_image = generate_fallback_image()
        
        return jsonify({
            'image_data': f'data:image/svg+xml;base64,{fallback_image}',
            'original_prompt': data.get('prompt', 'Unknown'),
            'enhanced_prompt': data.get('prompt', 'Unknown'),
            'source': 'emergency_fallback',
            'model': 'svg-generator',
            'timestamp': datetime.now().isoformat(),
            'message': f'Emergency fallback: {str(e)}'
        })

@app.route('/generate-video', methods=['POST', 'OPTIONS'])
def generate_video():
    """Generate video concept (placeholder for future implementation)"""
    
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.get_json()
        prompt = data.get('prompt', 'video concept')
        
        return jsonify({
            'message': 'Video generation coming soon!',
            'concept': f'Video concept for: {prompt}',
            'status': 'planned',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Video generation failed',
            'message': str(e)
        }), 500

@app.route('/generate-audio', methods=['POST', 'OPTIONS'])
def generate_audio():
    """Generate audio concept (placeholder for future implementation)"""
    
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.get_json()
        prompt = data.get('prompt', 'audio concept')
        
        return jsonify({
            'message': 'Audio generation coming soon!',
            'concept': f'Audio concept for: {prompt}',
            'status': 'planned',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Audio generation failed',
            'message': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'mythiq-media-creator',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
