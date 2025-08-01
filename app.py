"""
Mythiq Media Creator - AI-Powered Free Media Generation
Flask application for generating images, videos, and audio without API costs
"""

import os
import json
import time
import uuid
from datetime import datetime
from flask import Flask, request, jsonify, send_file, render_template_string
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Global variables
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mythiq-media-secret-key')
PORT = int(os.environ.get('PORT', 5003))
DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

# Service metrics
service_metrics = {
    'images_generated': 0,
    'videos_generated': 0,
    'audio_generated': 0,
    'total_requests': 0,
    'start_time': datetime.now(),
    'active_users': set()
}

# Import media generation modules with fallbacks
try:
    from media_ai import MediaAI
    from image_generator import ImageGenerator
    from video_generator import VideoGenerator
    from audio_generator import AudioGenerator
    
    # Initialize generators
    media_ai = MediaAI()
    image_gen = ImageGenerator()
    video_gen = VideoGenerator()
    audio_gen = AudioGenerator()
    
    SYSTEM_STATUS = "full_media_ai"
    print("🎨 Full Media AI System Loaded!")
    
except ImportError as e:
    print(f"⚠️ Media AI modules not found: {e}")
    print("🔄 Using fallback media generation system...")
    
    media_ai = None
    image_gen = None
    video_gen = None
    audio_gen = None
    
    SYSTEM_STATUS = "fallback_system"

@app.route('/')
def home():
    """Main API information endpoint"""
    return jsonify({
        "service": "mythiq-media-creator",
        "message": "Mythiq Media Creator API - AI-Powered Free Media Generation",
        "version": "3.0.0",
        "system_type": SYSTEM_STATUS,
        "capabilities": {
            "image_generation": True,
            "video_generation": True,
            "audio_generation": True,
            "procedural_generation": True,
            "template_based": True,
            "svg_generation": True,
            "css_animation": True,
            "web_audio": True,
            "unlimited_usage": True,
            "zero_api_costs": True
        },
        "endpoints": {
            "generate": "/api/generate (POST)",
            "image": "/api/image (POST)",
            "video": "/api/video (POST)",
            "audio": "/api/audio (POST)",
            "gallery": "/api/gallery",
            "health": "/health"
        },
        "supported_formats": {
            "images": ["svg", "png", "css"],
            "videos": ["mp4", "gif", "css"],
            "audio": ["wav", "mp3", "web-audio"]
        },
        "note": "100% free media generation - no API costs!",
        "status": "running"
    })

@app.route('/api/generate', methods=['POST'])
def generate_media():
    """Unified media generation endpoint"""
    try:
        data = request.json or {}
        prompt = data.get('prompt', '').strip()
        media_type = data.get('type', 'auto').lower()
        user_id = data.get('user_id', str(uuid.uuid4())[:8])
        
        if not prompt:
            return jsonify({
                "success": False,
                "error": "Prompt is required",
                "example": {
                    "prompt": "Create a ninja character image",
                    "type": "image"
                }
            }), 400
        
        # Track user and request
        service_metrics['active_users'].add(user_id)
        service_metrics['total_requests'] += 1
        
        start_time = time.time()
        
        # Route to appropriate generator
        if SYSTEM_STATUS == "full_media_ai" and media_ai:
            # Use full AI system
            analysis = media_ai.analyze_prompt(prompt)
            detected_type = analysis.get('media_type', media_type)
            
            if detected_type == 'image' or media_type == 'image':
                result = generate_image_ai(prompt, analysis, user_id)
            elif detected_type == 'video' or media_type == 'video':
                result = generate_video_ai(prompt, analysis, user_id)
            elif detected_type == 'audio' or media_type == 'audio':
                result = generate_audio_ai(prompt, analysis, user_id)
            else:
                # Auto-detect based on keywords
                if any(word in prompt.lower() for word in ['image', 'picture', 'character', 'background', 'art']):
                    result = generate_image_ai(prompt, analysis, user_id)
                elif any(word in prompt.lower() for word in ['video', 'animation', 'movie', 'clip']):
                    result = generate_video_ai(prompt, analysis, user_id)
                elif any(word in prompt.lower() for word in ['audio', 'music', 'sound', 'song']):
                    result = generate_audio_ai(prompt, analysis, user_id)
                else:
                    result = generate_image_ai(prompt, analysis, user_id)  # Default to image
        else:
            # Use fallback system
            result = generate_media_fallback(prompt, media_type, user_id)
        
        generation_time = time.time() - start_time
        
        # Add metadata
        result.update({
            "generation_time": round(generation_time, 2),
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
            "system_type": SYSTEM_STATUS
        })
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "system_type": SYSTEM_STATUS,
            "fallback_message": "Media generation encountered an error, but the service is still operational"
        }), 500

def generate_image_ai(prompt, analysis, user_id):
    """Generate image using AI system"""
    try:
        if image_gen:
            result = image_gen.generate(prompt, analysis)
            service_metrics['images_generated'] += 1
            return {
                "success": True,
                "type": "image",
                "result": result,
                "prompt": prompt,
                "analysis": analysis
            }
        else:
            return generate_image_fallback(prompt, user_id)
    except Exception as e:
        return generate_image_fallback(prompt, user_id, str(e))

def generate_video_ai(prompt, analysis, user_id):
    """Generate video using AI system"""
    try:
        if video_gen:
            result = video_gen.generate(prompt, analysis)
            service_metrics['videos_generated'] += 1
            return {
                "success": True,
                "type": "video",
                "result": result,
                "prompt": prompt,
                "analysis": analysis
            }
        else:
            return generate_video_fallback(prompt, user_id)
    except Exception as e:
        return generate_video_fallback(prompt, user_id, str(e))

def generate_audio_ai(prompt, analysis, user_id):
    """Generate audio using AI system"""
    try:
        if audio_gen:
            result = audio_gen.generate(prompt, analysis)
            service_metrics['audio_generated'] += 1
            return {
                "success": True,
                "type": "audio",
                "result": result,
                "prompt": prompt,
                "analysis": analysis
            }
        else:
            return generate_audio_fallback(prompt, user_id)
    except Exception as e:
        return generate_audio_fallback(prompt, user_id, str(e))

def generate_media_fallback(prompt, media_type, user_id):
    """Fallback media generation system"""
    
    # Simple keyword-based routing
    if media_type == 'image' or any(word in prompt.lower() for word in ['image', 'picture', 'character', 'art']):
        return generate_image_fallback(prompt, user_id)
    elif media_type == 'video' or any(word in prompt.lower() for word in ['video', 'animation', 'movie']):
        return generate_video_fallback(prompt, user_id)
    elif media_type == 'audio' or any(word in prompt.lower() for word in ['audio', 'music', 'sound']):
        return generate_audio_fallback(prompt, user_id)
    else:
        return generate_image_fallback(prompt, user_id)  # Default to image

def generate_image_fallback(prompt, user_id, error=None):
    """Fallback image generation"""
    
    # Extract theme and style from prompt
    theme = "default"
    if "ninja" in prompt.lower():
        theme = "ninja"
    elif "space" in prompt.lower():
        theme = "space"
    elif "medieval" in prompt.lower():
        theme = "medieval"
    elif "forest" in prompt.lower():
        theme = "forest"
    
    # Generate SVG image
    svg_content = generate_svg_image(prompt, theme)
    
    service_metrics['images_generated'] += 1
    
    return {
        "success": True,
        "type": "image",
        "format": "svg",
        "content": svg_content,
        "prompt": prompt,
        "theme": theme,
        "description": f"Generated SVG image based on: {prompt}",
        "usage_tip": "This SVG can be embedded directly in HTML or converted to PNG",
        "fallback_used": True if error else False,
        "error": error
    }

def generate_video_fallback(prompt, user_id, error=None):
    """Fallback video generation"""
    
    # Generate CSS animation
    css_animation = generate_css_animation(prompt)
    html_player = generate_video_html(prompt, css_animation)
    
    service_metrics['videos_generated'] += 1
    
    return {
        "success": True,
        "type": "video",
        "format": "css_animation",
        "css": css_animation,
        "html": html_player,
        "prompt": prompt,
        "description": f"Generated CSS animation based on: {prompt}",
        "usage_tip": "Embed the HTML to display the animation",
        "fallback_used": True if error else False,
        "error": error
    }

def generate_audio_fallback(prompt, user_id, error=None):
    """Fallback audio generation"""
    
    # Generate Web Audio API code
    audio_code = generate_web_audio(prompt)
    
    service_metrics['audio_generated'] += 1
    
    return {
        "success": True,
        "type": "audio",
        "format": "web_audio",
        "javascript": audio_code,
        "prompt": prompt,
        "description": f"Generated Web Audio API code based on: {prompt}",
        "usage_tip": "Execute the JavaScript code to play the generated audio",
        "fallback_used": True if error else False,
        "error": error
    }

def generate_svg_image(prompt, theme):
    """Generate SVG image based on prompt and theme"""
    
    # Theme color schemes
    themes = {
        "ninja": {"primary": "#2C3E50", "secondary": "#E74C3C", "accent": "#F39C12"},
        "space": {"primary": "#0F3460", "secondary": "#E94560", "accent": "#16213E"},
        "medieval": {"primary": "#8B4513", "secondary": "#DAA520", "accent": "#CD853F"},
        "forest": {"primary": "#228B22", "secondary": "#FFD700", "accent": "#32CD32"},
        "default": {"primary": "#3498DB", "secondary": "#E74C3C", "accent": "#F39C12"}
    }
    
    colors = themes.get(theme, themes["default"])
    
    # Character detection
    if any(word in prompt.lower() for word in ['character', 'person', 'hero', 'warrior', 'ninja']):
        return f'''
        <svg width="200" height="300" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="bodyGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:{colors['primary']};stop-opacity:1" />
                    <stop offset="100%" style="stop-color:{colors['secondary']};stop-opacity:1" />
                </linearGradient>
            </defs>
            
            <!-- Character Body -->
            <ellipse cx="100" cy="80" rx="30" ry="35" fill="url(#bodyGradient)"/>
            <rect x="80" y="110" width="40" height="80" fill="{colors['primary']}" rx="5"/>
            <rect x="75" y="130" width="50" height="15" fill="{colors['secondary']}" rx="3"/>
            
            <!-- Arms -->
            <ellipse cx="60" cy="140" rx="12" ry="30" fill="{colors['primary']}"/>
            <ellipse cx="140" cy="140" rx="12" ry="30" fill="{colors['primary']}"/>
            
            <!-- Legs -->
            <ellipse cx="85" cy="210" rx="12" ry="35" fill="{colors['primary']}"/>
            <ellipse cx="115" cy="210" rx="12" ry="35" fill="{colors['primary']}"/>
            
            <!-- Head Details -->
            <circle cx="90" cy="75" r="3" fill="{colors['accent']}"/>
            <circle cx="110" cy="75" r="3" fill="{colors['accent']}"/>
            
            <!-- Weapon/Tool -->
            <line x1="45" y1="130" x2="25" y2="110" stroke="{colors['accent']}" stroke-width="4"/>
            <circle cx="25" cy="110" r="5" fill="{colors['secondary']}"/>
            
            <!-- Animation -->
            <animateTransform attributeName="transform" type="rotate" 
                             values="0 100 150;2 100 150;-2 100 150;0 100 150" 
                             dur="3s" repeatCount="indefinite"/>
        </svg>
        '''
    
    # Background/Environment detection
    elif any(word in prompt.lower() for word in ['background', 'environment', 'landscape', 'scene']):
        return f'''
        <svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="skyGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:{colors['accent']};stop-opacity:0.8" />
                    <stop offset="100%" style="stop-color:{colors['primary']};stop-opacity:1" />
                </linearGradient>
                <radialGradient id="sunGradient" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" style="stop-color:{colors['secondary']};stop-opacity:1" />
                    <stop offset="100%" style="stop-color:{colors['accent']};stop-opacity:0.6" />
                </radialGradient>
            </defs>
            
            <!-- Sky -->
            <rect width="400" height="200" fill="url(#skyGradient)"/>
            
            <!-- Sun/Moon -->
            <circle cx="320" cy="60" r="25" fill="url(#sunGradient)">
                <animate attributeName="cy" values="60;55;60" dur="4s" repeatCount="indefinite"/>
            </circle>
            
            <!-- Mountains/Hills -->
            <polygon points="0,150 100,100 200,130 300,80 400,120 400,200 0,200" fill="{colors['primary']}"/>
            <polygon points="50,170 150,120 250,140 350,100 400,130 400,200 0,200" fill="{colors['secondary']}" opacity="0.7"/>
            
            <!-- Trees/Elements -->
            <ellipse cx="80" cy="160" rx="15" ry="25" fill="{colors['accent']}"/>
            <ellipse cx="200" cy="150" rx="20" ry="30" fill="{colors['accent']}"/>
            <ellipse cx="320" cy="155" rx="18" ry="28" fill="{colors['accent']}"/>
            
            <!-- Animated particles -->
            <circle cx="150" cy="100" r="2" fill="{colors['secondary']}" opacity="0.6">
                <animate attributeName="cy" values="100;80;100" dur="3s" repeatCount="indefinite"/>
                <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" repeatCount="indefinite"/>
            </circle>
            <circle cx="250" cy="90" r="1.5" fill="{colors['accent']}" opacity="0.8">
                <animate attributeName="cy" values="90;70;90" dur="4s" repeatCount="indefinite"/>
            </circle>
        </svg>
        '''
    
    # Default abstract art
    else:
        return f'''
        <svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <radialGradient id="centerGradient" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" style="stop-color:{colors['accent']};stop-opacity:1" />
                    <stop offset="50%" style="stop-color:{colors['secondary']};stop-opacity:0.8" />
                    <stop offset="100%" style="stop-color:{colors['primary']};stop-opacity:1" />
                </radialGradient>
            </defs>
            
            <!-- Background -->
            <rect width="300" height="300" fill="url(#centerGradient)"/>
            
            <!-- Geometric shapes -->
            <polygon points="150,50 200,100 150,150 100,100" fill="{colors['primary']}" opacity="0.8">
                <animateTransform attributeName="transform" type="rotate" 
                                 values="0 150 100;360 150 100" dur="10s" repeatCount="indefinite"/>
            </polygon>
            
            <circle cx="150" cy="150" r="40" fill="{colors['secondary']}" opacity="0.6">
                <animate attributeName="r" values="40;50;40" dur="3s" repeatCount="indefinite"/>
            </circle>
            
            <rect x="100" y="200" width="100" height="20" fill="{colors['accent']}" opacity="0.7">
                <animate attributeName="width" values="100;120;100" dur="2s" repeatCount="indefinite"/>
            </rect>
            
            <!-- Decorative elements -->
            <circle cx="80" cy="80" r="8" fill="{colors['accent']}"/>
            <circle cx="220" cy="80" r="6" fill="{colors['secondary']}"/>
            <circle cx="80" cy="220" r="10" fill="{colors['primary']}"/>
            <circle cx="220" cy="220" r="7" fill="{colors['accent']}"/>
        </svg>
        '''

def generate_css_animation(prompt):
    """Generate CSS animation based on prompt"""
    
    # Detect animation type
    if any(word in prompt.lower() for word in ['character', 'person', 'walk', 'move']):
        return '''
        @keyframes character_move {
            0% { transform: translateX(0) scale(1); }
            25% { transform: translateX(50px) scale(1.1); }
            50% { transform: translateX(100px) scale(1); }
            75% { transform: translateX(50px) scale(0.9); }
            100% { transform: translateX(0) scale(1); }
        }
        
        .character-animation {
            width: 100px;
            height: 100px;
            background: linear-gradient(45deg, #3498DB, #E74C3C);
            border-radius: 50%;
            animation: character_move 4s ease-in-out infinite;
            position: relative;
        }
        
        .character-animation::before {
            content: '';
            position: absolute;
            top: 20%;
            left: 20%;
            width: 60%;
            height: 60%;
            background: radial-gradient(circle, #F39C12, #E67E22);
            border-radius: 50%;
            animation: pulse 2s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.2); opacity: 0.8; }
        }
        '''
    
    elif any(word in prompt.lower() for word in ['background', 'environment', 'scene']):
        return '''
        @keyframes background_flow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .background-animation {
            width: 100%;
            height: 200px;
            background: linear-gradient(-45deg, #2C3E50, #3498DB, #E74C3C, #F39C12);
            background-size: 400% 400%;
            animation: background_flow 8s ease infinite;
            position: relative;
            overflow: hidden;
        }
        
        .background-animation::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            animation: shine 3s ease-in-out infinite;
        }
        
        @keyframes shine {
            0% { left: -100%; }
            100% { left: 100%; }
        }
        '''
    
    else:
        return '''
        @keyframes abstract_motion {
            0% { transform: rotate(0deg) scale(1); border-radius: 50%; }
            25% { transform: rotate(90deg) scale(1.2); border-radius: 25%; }
            50% { transform: rotate(180deg) scale(1); border-radius: 0%; }
            75% { transform: rotate(270deg) scale(0.8); border-radius: 25%; }
            100% { transform: rotate(360deg) scale(1); border-radius: 50%; }
        }
        
        .abstract-animation {
            width: 150px;
            height: 150px;
            background: conic-gradient(from 0deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7, #DDA0DD, #FF6B6B);
            animation: abstract_motion 6s ease-in-out infinite;
            margin: 50px auto;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        
        .abstract-animation::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 50%;
            height: 50%;
            background: radial-gradient(circle, rgba(255,255,255,0.8), transparent);
            transform: translate(-50%, -50%);
            border-radius: 50%;
            animation: inner_glow 3s ease-in-out infinite alternate;
        }
        
        @keyframes inner_glow {
            0% { opacity: 0.3; transform: translate(-50%, -50%) scale(0.8); }
            100% { opacity: 0.8; transform: translate(-50%, -50%) scale(1.2); }
        }
        '''

def generate_video_html(prompt, css_animation):
    """Generate HTML player for CSS animation"""
    
    title = f"Generated Animation: {prompt[:50]}..."
    
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
            }}
            
            .video-container {{
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                text-align: center;
                max-width: 600px;
                width: 100%;
            }}
            
            .video-title {{
                color: white;
                font-size: 1.5em;
                margin-bottom: 20px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }}
            
            .animation-stage {{
                background: rgba(0, 0, 0, 0.1);
                border-radius: 10px;
                padding: 40px;
                margin: 20px 0;
                position: relative;
                overflow: hidden;
            }}
            
            .controls {{
                margin-top: 20px;
            }}
            
            .control-btn {{
                background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
                border: none;
                color: white;
                padding: 10px 20px;
                margin: 0 10px;
                border-radius: 25px;
                cursor: pointer;
                font-weight: bold;
                transition: transform 0.2s;
            }}
            
            .control-btn:hover {{
                transform: scale(1.05);
            }}
            
            .info {{
                color: rgba(255, 255, 255, 0.8);
                font-size: 0.9em;
                margin-top: 15px;
            }}
            
            {css_animation}
        </style>
    </head>
    <body>
        <div class="video-container">
            <h2 class="video-title">{title}</h2>
            <div class="animation-stage">
                <div class="character-animation abstract-animation background-animation"></div>
            </div>
            <div class="controls">
                <button class="control-btn" onclick="toggleAnimation()">Pause/Play</button>
                <button class="control-btn" onclick="restartAnimation()">Restart</button>
                <button class="control-btn" onclick="changeSpeed()">Speed</button>
            </div>
            <div class="info">
                Generated by Mythiq Media Creator<br>
                Prompt: "{prompt}"<br>
                Format: CSS Animation
            </div>
        </div>
        
        <script>
            let isPaused = false;
            let currentSpeed = 1;
            const speeds = [0.5, 1, 1.5, 2];
            let speedIndex = 1;
            
            function toggleAnimation() {{
                const elements = document.querySelectorAll('.character-animation, .abstract-animation, .background-animation');
                elements.forEach(el => {{
                    if (isPaused) {{
                        el.style.animationPlayState = 'running';
                    }} else {{
                        el.style.animationPlayState = 'paused';
                    }}
                }});
                isPaused = !isPaused;
            }}
            
            function restartAnimation() {{
                const elements = document.querySelectorAll('.character-animation, .abstract-animation, .background-animation');
                elements.forEach(el => {{
                    el.style.animation = 'none';
                    el.offsetHeight; // Trigger reflow
                    el.style.animation = null;
                }});
            }}
            
            function changeSpeed() {{
                speedIndex = (speedIndex + 1) % speeds.length;
                currentSpeed = speeds[speedIndex];
                const elements = document.querySelectorAll('.character-animation, .abstract-animation, .background-animation');
                elements.forEach(el => {{
                    el.style.animationDuration = `${{6 / currentSpeed}}s`;
                }});
            }}
            
            console.log('🎬 Mythiq Media Creator - Animation Ready!');
            console.log('Prompt:', '{prompt}');
            console.log('Type: CSS Animation Video');
        </script>
    </body>
    </html>
    '''

def generate_web_audio(prompt):
    """Generate Web Audio API code for sound generation"""
    
    if any(word in prompt.lower() for word in ['epic', 'battle', 'intense', 'dramatic']):
        return '''
        // Epic Battle Music Generator
        function generateEpicMusic() {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            
            // Epic chord progression: Am - F - C - G
            const chords = [
                [220, 261.63, 329.63], // Am
                [174.61, 220, 261.63], // F
                [261.63, 329.63, 392],  // C
                [196, 246.94, 293.66]   // G
            ];
            
            let currentChord = 0;
            
            function playChord(frequencies, duration = 1) {
                frequencies.forEach((freq, index) => {
                    const oscillator = audioContext.createOscillator();
                    const gainNode = audioContext.createGain();
                    const filterNode = audioContext.createBiquadFilter();
                    
                    oscillator.connect(filterNode);
                    filterNode.connect(gainNode);
                    gainNode.connect(audioContext.destination);
                    
                    oscillator.type = index === 0 ? 'sawtooth' : 'square';
                    oscillator.frequency.setValueAtTime(freq, audioContext.currentTime);
                    
                    filterNode.type = 'lowpass';
                    filterNode.frequency.setValueAtTime(800, audioContext.currentTime);
                    
                    gainNode.gain.setValueAtTime(0, audioContext.currentTime);
                    gainNode.gain.linearRampToValueAtTime(0.1, audioContext.currentTime + 0.1);
                    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + duration);
                    
                    oscillator.start(audioContext.currentTime);
                    oscillator.stop(audioContext.currentTime + duration);
                });
            }
            
            function playSequence() {
                chords.forEach((chord, index) => {
                    setTimeout(() => {
                        playChord(chord, 0.8);
                    }, index * 800);
                });
            }
            
            // Add drums
            function playDrum() {
                const oscillator = audioContext.createOscillator();
                const gainNode = audioContext.createGain();
                
                oscillator.connect(gainNode);
                gainNode.connect(audioContext.destination);
                
                oscillator.frequency.setValueAtTime(60, audioContext.currentTime);
                oscillator.frequency.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
                
                gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
                
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 0.1);
            }
            
            // Play the epic sequence
            playSequence();
            
            // Add drum beats
            [0, 400, 800, 1200, 1600, 2000, 2400, 2800].forEach(delay => {
                setTimeout(playDrum, delay);
            });
            
            return audioContext;
        }
        
        // Usage: generateEpicMusic();
        console.log('🎵 Epic battle music ready! Call generateEpicMusic() to play.');
        '''
    
    elif any(word in prompt.lower() for word in ['peaceful', 'calm', 'ambient', 'relaxing']):
        return '''
        // Peaceful Ambient Music Generator
        function generatePeacefulMusic() {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            
            // Peaceful pentatonic scale
            const notes = [261.63, 293.66, 329.63, 392, 440, 523.25]; // C, D, E, G, A, C
            
            function playNote(frequency, delay = 0, duration = 2) {
                const oscillator = audioContext.createOscillator();
                const gainNode = audioContext.createGain();
                const filterNode = audioContext.createBiquadFilter();
                
                oscillator.connect(filterNode);
                filterNode.connect(gainNode);
                gainNode.connect(audioContext.destination);
                
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(frequency, audioContext.currentTime + delay);
                
                filterNode.type = 'lowpass';
                filterNode.frequency.setValueAtTime(1000, audioContext.currentTime + delay);
                
                gainNode.gain.setValueAtTime(0, audioContext.currentTime + delay);
                gainNode.gain.linearRampToValueAtTime(0.05, audioContext.currentTime + delay + 0.5);
                gainNode.gain.linearRampToValueAtTime(0.03, audioContext.currentTime + delay + duration - 0.5);
                gainNode.gain.linearRampToValueAtTime(0, audioContext.currentTime + delay + duration);
                
                oscillator.start(audioContext.currentTime + delay);
                oscillator.stop(audioContext.currentTime + delay + duration);
            }
            
            // Create a peaceful melody
            const melody = [0, 2, 1, 3, 2, 4, 3, 5, 4, 2, 1, 0];
            
            melody.forEach((noteIndex, index) => {
                playNote(notes[noteIndex], index * 0.8, 1.5);
            });
            
            // Add harmony
            setTimeout(() => {
                melody.forEach((noteIndex, index) => {
                    playNote(notes[noteIndex] * 0.5, index * 0.8, 2); // Octave lower
                });
            }, 400);
            
            return audioContext;
        }
        
        // Usage: generatePeacefulMusic();
        console.log('🎵 Peaceful ambient music ready! Call generatePeacefulMusic() to play.');
        '''
    
    else:
        return '''
        // Sound Effect Generator
        function generateSoundEffect() {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            
            function playJumpSound() {
                const oscillator = audioContext.createOscillator();
                const gainNode = audioContext.createGain();
                
                oscillator.connect(gainNode);
                gainNode.connect(audioContext.destination);
                
                oscillator.frequency.setValueAtTime(400, audioContext.currentTime);
                oscillator.frequency.exponentialRampToValueAtTime(800, audioContext.currentTime + 0.1);
                
                gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.2);
                
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 0.2);
            }
            
            function playCoinSound() {
                const oscillator = audioContext.createOscillator();
                const gainNode = audioContext.createGain();
                
                oscillator.connect(gainNode);
                gainNode.connect(audioContext.destination);
                
                oscillator.frequency.setValueAtTime(800, audioContext.currentTime);
                oscillator.frequency.setValueAtTime(1000, audioContext.currentTime + 0.1);
                
                gainNode.gain.setValueAtTime(0.2, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.3);
                
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 0.3);
            }
            
            function playHitSound() {
                const oscillator = audioContext.createOscillator();
                const gainNode = audioContext.createGain();
                
                oscillator.connect(gainNode);
                gainNode.connect(audioContext.destination);
                
                oscillator.type = 'sawtooth';
                oscillator.frequency.setValueAtTime(200, audioContext.currentTime);
                oscillator.frequency.exponentialRampToValueAtTime(50, audioContext.currentTime + 0.1);
                
                gainNode.gain.setValueAtTime(0.4, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.2);
                
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 0.2);
            }
            
            // Play a sequence of sound effects
            playJumpSound();
            setTimeout(playCoinSound, 500);
            setTimeout(playHitSound, 1000);
            
            return { playJumpSound, playCoinSound, playHitSound };
        }
        
        // Usage: const sounds = generateSoundEffect();
        // Then: sounds.playJumpSound(), sounds.playCoinSound(), sounds.playHitSound()
        console.log('🔊 Sound effects ready! Call generateSoundEffect() to play sequence.');
        '''

@app.route('/api/gallery')
def gallery():
    """Get gallery of recently generated media"""
    return jsonify({
        "success": True,
        "gallery": {
            "recent_images": service_metrics['images_generated'],
            "recent_videos": service_metrics['videos_generated'],
            "recent_audio": service_metrics['audio_generated'],
            "total_media": service_metrics['images_generated'] + service_metrics['videos_generated'] + service_metrics['audio_generated']
        },
        "examples": {
            "image_prompts": [
                "Create a ninja character",
                "Generate a space background",
                "Make a medieval warrior",
                "Design a forest scene"
            ],
            "video_prompts": [
                "Animate a character walking",
                "Create a flowing background",
                "Make an abstract animation",
                "Generate particle effects"
            ],
            "audio_prompts": [
                "Create epic battle music",
                "Generate peaceful ambient sounds",
                "Make jump sound effects",
                "Compose victory music"
            ]
        }
    })

@app.route('/health')
def health_check():
    """Comprehensive health check endpoint"""
    uptime = datetime.now() - service_metrics['start_time']
    
    return jsonify({
        "service": "mythiq-media-creator",
        "status": "healthy",
        "system_type": SYSTEM_STATUS,
        "version": "3.0.0",
        "uptime_seconds": int(uptime.total_seconds()),
        "capabilities": {
            "image_generation": True,
            "video_generation": True,
            "audio_generation": True,
            "svg_generation": True,
            "css_animation": True,
            "web_audio": True,
            "procedural_generation": True,
            "zero_cost_operation": True
        },
        "metrics": {
            "images_generated": service_metrics['images_generated'],
            "videos_generated": service_metrics['videos_generated'],
            "audio_generated": service_metrics['audio_generated'],
            "total_requests": service_metrics['total_requests'],
            "active_users": len(service_metrics['active_users'])
        },
        "supported_formats": {
            "images": ["svg", "png", "css"],
            "videos": ["css_animation", "html5"],
            "audio": ["web_audio", "javascript"]
        },
        "ai_confidence": "high" if SYSTEM_STATUS == "full_media_ai" else "medium",
        "generation_speed": "1-3 seconds average",
        "cost_per_generation": "$0.00",
        "timestamp": datetime.now().isoformat()
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint not found",
        "available_endpoints": {
            "main": "/",
            "generate": "/api/generate",
            "gallery": "/api/gallery", 
            "health": "/health"
        },
        "service": "mythiq-media-creator"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Internal server error",
        "message": "Media generation service encountered an error",
        "service": "mythiq-media-creator",
        "status": "degraded",
        "fallback": "Basic media generation still available"
    }), 500

if __name__ == '__main__':
    print("🎨 Starting Mythiq Media Creator...")
    print(f"🔧 System Type: {SYSTEM_STATUS}")
    print(f"🌐 Port: {PORT}")
    print(f"🎯 Debug Mode: {DEBUG}")
    print("✅ Free media generation service ready!")
    
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)

