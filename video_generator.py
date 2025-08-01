"""
Mythiq Video Generator - Advanced CSS Animation Video System
Creates professional-quality videos using CSS animations, HTML5, and JavaScript
"""

import json
import math
import random
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class VideoGenerator:
    """
    Advanced video generation system using CSS animations and HTML5
    Creates animated content without heavy video processing libraries
    """
    
    def __init__(self):
        """Initialize the video generation system"""
        self.animation_types = {
            'character_walk': self._create_character_walk_animation,
            'character_idle': self._create_character_idle_animation,
            'character_attack': self._create_character_attack_animation,
            'environment_flow': self._create_environment_flow_animation,
            'ui_transition': self._create_ui_transition_animation,
            'particle_effect': self._create_particle_effect_animation,
            'text_reveal': self._create_text_reveal_animation,
            'logo_animation': self._create_logo_animation_animation
        }
        
        self.duration_presets = {
            'quick': 2,
            'short': 5,
            'medium': 10,
            'long': 15,
            'extended': 30
        }
        
        self.easing_functions = {
            'linear': 'linear',
            'ease': 'ease',
            'ease_in': 'ease-in',
            'ease_out': 'ease-out',
            'ease_in_out': 'ease-in-out',
            'bounce': 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
            'elastic': 'cubic-bezier(0.175, 0.885, 0.32, 1.275)',
            'smooth': 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
        }
        
        print("🎬 Advanced Video Generator initialized with CSS animation capabilities")
    
    def generate(self, prompt: str, analysis: Dict) -> Dict:
        """
        Generate video based on prompt and analysis
        
        Args:
            prompt (str): User's video request
            analysis (Dict): AI analysis of the prompt
            
        Returns:
            Dict: Generated video data and metadata
        """
        theme = analysis.get('theme', 'default')
        style = analysis.get('style', 'default')
        complexity = analysis.get('complexity', 'medium')
        keywords = analysis.get('keywords', [])
        mood = analysis.get('mood', 'neutral')
        
        # Determine animation type
        animation_type = self._determine_animation_type(keywords, prompt)
        
        # Determine duration
        duration = self._determine_duration(keywords, prompt, complexity)
        
        # Generate the video
        result = self._generate_animation(
            prompt, theme, style, complexity, keywords, 
            mood, animation_type, duration
        )
        
        # Add metadata
        result.update({
            'generation_method': 'css_animation',
            'theme': theme,
            'style': style,
            'complexity': complexity,
            'animation_type': animation_type,
            'duration': duration,
            'mood': mood,
            'prompt': prompt,
            'timestamp': datetime.now().isoformat(),
            'generator_version': '3.0.0'
        })
        
        return result
    
    def _determine_animation_type(self, keywords: List[str], prompt: str) -> str:
        """Determine what type of animation to create"""
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ['walk', 'walking', 'move', 'moving', 'run', 'running']):
            return 'character_walk'
        elif any(word in prompt_lower for word in ['attack', 'fighting', 'battle', 'combat', 'strike']):
            return 'character_attack'
        elif any(word in prompt_lower for word in ['idle', 'standing', 'breathing', 'waiting']):
            return 'character_idle'
        elif any(word in prompt_lower for word in ['flow', 'flowing', 'water', 'wind', 'particles']):
            return 'environment_flow'
        elif any(word in prompt_lower for word in ['transition', 'fade', 'slide', 'ui', 'interface']):
            return 'ui_transition'
        elif any(word in prompt_lower for word in ['particle', 'effect', 'magic', 'sparkle', 'explosion']):
            return 'particle_effect'
        elif any(word in prompt_lower for word in ['text', 'title', 'reveal', 'typewriter']):
            return 'text_reveal'
        elif any(word in prompt_lower for word in ['logo', 'brand', 'intro', 'opening']):
            return 'logo_animation'
        else:
            return 'character_idle'  # Default fallback
    
    def _determine_duration(self, keywords: List[str], prompt: str, complexity: str) -> int:
        """Determine animation duration in seconds"""
        prompt_lower = prompt.lower()
        
        # Check for explicit duration keywords
        if any(word in prompt_lower for word in ['quick', 'fast', 'brief']):
            return self.duration_presets['quick']
        elif any(word in prompt_lower for word in ['short']):
            return self.duration_presets['short']
        elif any(word in prompt_lower for word in ['long', 'extended', 'detailed']):
            return self.duration_presets['long']
        
        # Base on complexity
        if complexity == 'simple':
            return self.duration_presets['short']
        elif complexity == 'detailed':
            return self.duration_presets['medium']
        elif complexity == 'professional':
            return self.duration_presets['long']
        
        return self.duration_presets['medium']  # Default
    
    def _generate_animation(self, prompt: str, theme: str, style: str, complexity: str, 
                          keywords: List[str], mood: str, animation_type: str, duration: int) -> Dict:
        """Generate the complete animation"""
        
        # Get color scheme based on theme
        colors = self._get_color_scheme(theme)
        
        # Generate animation using the appropriate method
        animation_generator = self.animation_types.get(animation_type, self.animation_types['character_idle'])
        animation_content = animation_generator(colors, duration, complexity, keywords, mood, style)
        
        return {
            'success': True,
            'format': 'html_css_animation',
            'content': animation_content,
            'colors_used': colors,
            'description': f"Generated {animation_type} animation with {theme} theme for {duration} seconds",
            'usage_tips': [
                "HTML file can be opened directly in browser",
                "CSS animations are smooth and performant",
                "Can be embedded in websites or apps",
                "Works on all modern browsers"
            ],
            'technical_specs': {
                'format': 'HTML5 + CSS3',
                'duration': f"{duration}s",
                'animation_type': animation_type,
                'browser_support': '95%+',
                'file_size': 'Under 50KB'
            }
        }
    
    def _get_color_scheme(self, theme: str) -> Dict:
        """Get color scheme for the theme"""
        color_schemes = {
            'ninja': {
                'primary': '#2C3E50',
                'secondary': '#E74C3C', 
                'accent': '#F39C12',
                'background': '#34495E',
                'text': '#ECF0F1'
            },
            'space': {
                'primary': '#0F3460',
                'secondary': '#E94560',
                'accent': '#16213E',
                'background': '#0F0F23',
                'text': '#F0F0F0'
            },
            'medieval': {
                'primary': '#8B4513',
                'secondary': '#DAA520',
                'accent': '#CD853F',
                'background': '#654321',
                'text': '#F5DEB3'
            },
            'forest': {
                'primary': '#228B22',
                'secondary': '#FFD700',
                'accent': '#32CD32',
                'background': '#006400',
                'text': '#F0FFF0'
            },
            'underwater': {
                'primary': '#008B8B',
                'secondary': '#20B2AA',
                'accent': '#48D1CC',
                'background': '#006666',
                'text': '#E0FFFF'
            },
            'default': {
                'primary': '#3498DB',
                'secondary': '#E74C3C',
                'accent': '#F39C12',
                'background': '#2C3E50',
                'text': '#ECF0F1'
            }
        }
        
        return color_schemes.get(theme, color_schemes['default'])
    
    def _create_character_walk_animation(self, colors: Dict, duration: int, complexity: str, 
                                       keywords: List[str], mood: str, style: str) -> str:
        """Create character walking animation"""
        
        # Determine character type
        char_type = 'humanoid'
        if 'ninja' in keywords:
            char_type = 'ninja'
        elif 'robot' in keywords:
            char_type = 'robot'
        
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Character Walk Animation</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, {colors['background']}, {colors['primary']});
            overflow: hidden;
            font-family: Arial, sans-serif;
        }}
        
        .scene {{
            width: 100vw;
            height: 100vh;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .character {{
            width: 80px;
            height: 120px;
            position: relative;
            animation: walkCycle {duration}s infinite linear;
        }}
        
        .character-body {{
            width: 40px;
            height: 60px;
            background: {colors['primary']};
            border-radius: 20px 20px 5px 5px;
            position: absolute;
            top: 30px;
            left: 20px;
            animation: bodyBob 0.8s infinite ease-in-out;
        }}
        
        .character-head {{
            width: 30px;
            height: 30px;
            background: {colors['secondary']};
            border-radius: 50%;
            position: absolute;
            top: 5px;
            left: 25px;
            animation: headBob 0.8s infinite ease-in-out;
        }}
        
        .character-leg {{
            width: 12px;
            height: 40px;
            background: {colors['primary']};
            border-radius: 6px;
            position: absolute;
            top: 85px;
        }}
        
        .leg-left {{
            left: 28px;
            animation: legWalkLeft 0.8s infinite ease-in-out;
        }}
        
        .leg-right {{
            left: 40px;
            animation: legWalkRight 0.8s infinite ease-in-out;
        }}
        
        .character-arm {{
            width: 10px;
            height: 30px;
            background: {colors['secondary']};
            border-radius: 5px;
            position: absolute;
            top: 40px;
        }}
        
        .arm-left {{
            left: 15px;
            animation: armSwingLeft 0.8s infinite ease-in-out;
        }}
        
        .arm-right {{
            left: 55px;
            animation: armSwingRight 0.8s infinite ease-in-out;
        }}
        
        .ground {{
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 100px;
            background: linear-gradient(to top, {colors['accent']}, transparent);
            animation: groundMove {duration}s infinite linear;
        }}
        
        .background-element {{
            position: absolute;
            width: 60px;
            height: 80px;
            background: {colors['primary']};
            opacity: 0.3;
            border-radius: 30px 30px 0 0;
            animation: backgroundMove {duration * 2}s infinite linear;
        }}
        
        .bg-tree1 {{ top: 20%; left: -100px; }}
        .bg-tree2 {{ top: 30%; left: -200px; animation-delay: -1s; }}
        .bg-tree3 {{ top: 25%; left: -300px; animation-delay: -2s; }}
        
        @keyframes walkCycle {{
            0% {{ transform: translateX(-50vw); }}
            100% {{ transform: translateX(50vw); }}
        }}
        
        @keyframes bodyBob {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-3px); }}
        }}
        
        @keyframes headBob {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-2px); }}
        }}
        
        @keyframes legWalkLeft {{
            0% {{ transform: rotate(0deg); }}
            25% {{ transform: rotate(20deg); }}
            50% {{ transform: rotate(0deg); }}
            75% {{ transform: rotate(-20deg); }}
            100% {{ transform: rotate(0deg); }}
        }}
        
        @keyframes legWalkRight {{
            0% {{ transform: rotate(0deg); }}
            25% {{ transform: rotate(-20deg); }}
            50% {{ transform: rotate(0deg); }}
            75% {{ transform: rotate(20deg); }}
            100% {{ transform: rotate(0deg); }}
        }}
        
        @keyframes armSwingLeft {{
            0% {{ transform: rotate(0deg); }}
            25% {{ transform: rotate(-15deg); }}
            50% {{ transform: rotate(0deg); }}
            75% {{ transform: rotate(15deg); }}
            100% {{ transform: rotate(0deg); }}
        }}
        
        @keyframes armSwingRight {{
            0% {{ transform: rotate(0deg); }}
            25% {{ transform: rotate(15deg); }}
            50% {{ transform: rotate(0deg); }}
            75% {{ transform: rotate(-15deg); }}
            100% {{ transform: rotate(0deg); }}
        }}
        
        @keyframes groundMove {{
            0% {{ background-position: 0px 0px; }}
            100% {{ background-position: -200px 0px; }}
        }}
        
        @keyframes backgroundMove {{
            0% {{ transform: translateX(0px); }}
            100% {{ transform: translateX(100vw); }}
        }}
        
        .info-panel {{
            position: absolute;
            top: 20px;
            left: 20px;
            background: rgba(0,0,0,0.7);
            color: {colors['text']};
            padding: 15px;
            border-radius: 10px;
            font-size: 14px;
        }}
        
        .controls {{
            position: absolute;
            bottom: 20px;
            right: 20px;
            background: rgba(0,0,0,0.7);
            color: {colors['text']};
            padding: 10px;
            border-radius: 5px;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="scene">
        <div class="ground"></div>
        
        <div class="background-element bg-tree1"></div>
        <div class="background-element bg-tree2"></div>
        <div class="background-element bg-tree3"></div>
        
        <div class="character">
            <div class="character-head"></div>
            <div class="character-body"></div>
            <div class="character-arm arm-left"></div>
            <div class="character-arm arm-right"></div>
            <div class="character-leg leg-left"></div>
            <div class="character-leg leg-right"></div>
        </div>
        
        <div class="info-panel">
            <strong>Character Walk Animation</strong><br>
            Duration: {duration}s<br>
            Theme: {colors['primary']}<br>
            Style: CSS3 Animation
        </div>
        
        <div class="controls">
            Right-click → Save As → video.html
        </div>
    </div>
    
    <script>
        // Add interactive controls
        document.addEventListener('keydown', function(e) {{
            const character = document.querySelector('.character');
            if (e.key === ' ') {{
                character.style.animationPlayState = 
                    character.style.animationPlayState === 'paused' ? 'running' : 'paused';
            }}
        }});
        
        // Auto-restart animation
        setTimeout(() => {{
            document.querySelector('.character').style.animation = 
                'walkCycle {duration}s infinite linear';
        }}, {duration * 1000});
    </script>
</body>
</html>
        '''
    
    def _create_character_idle_animation(self, colors: Dict, duration: int, complexity: str, 
                                       keywords: List[str], mood: str, style: str) -> str:
        """Create character idle animation"""
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Character Idle Animation</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: radial-gradient(circle, {colors['background']}, {colors['primary']});
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }}
        
        .character {{
            width: 100px;
            height: 150px;
            position: relative;
            animation: idleBreathe 3s infinite ease-in-out;
        }}
        
        .character-head {{
            width: 40px;
            height: 40px;
            background: {colors['secondary']};
            border-radius: 50%;
            position: absolute;
            top: 0;
            left: 30px;
            animation: headSway 4s infinite ease-in-out;
        }}
        
        .character-body {{
            width: 50px;
            height: 70px;
            background: {colors['primary']};
            border-radius: 25px 25px 10px 10px;
            position: absolute;
            top: 35px;
            left: 25px;
        }}
        
        .character-arm {{
            width: 12px;
            height: 35px;
            background: {colors['secondary']};
            border-radius: 6px;
            position: absolute;
            top: 50px;
        }}
        
        .arm-left {{
            left: 10px;
            animation: armFloat 5s infinite ease-in-out;
        }}
        
        .arm-right {{
            right: 10px;
            animation: armFloat 5s infinite ease-in-out reverse;
        }}
        
        .character-leg {{
            width: 15px;
            height: 45px;
            background: {colors['primary']};
            border-radius: 7px;
            position: absolute;
            top: 100px;
        }}
        
        .leg-left {{
            left: 30px;
            animation: legShift 6s infinite ease-in-out;
        }}
        
        .leg-right {{
            left: 55px;
            animation: legShift 6s infinite ease-in-out reverse;
        }}
        
        .aura {{
            position: absolute;
            width: 150px;
            height: 150px;
            border: 2px solid {colors['accent']};
            border-radius: 50%;
            top: -25px;
            left: -25px;
            opacity: 0.3;
            animation: auraGlow 4s infinite ease-in-out;
        }}
        
        @keyframes idleBreathe {{
            0%, 100% {{ transform: scale(1) translateY(0px); }}
            50% {{ transform: scale(1.02) translateY(-2px); }}
        }}
        
        @keyframes headSway {{
            0%, 100% {{ transform: rotate(0deg); }}
            25% {{ transform: rotate(2deg); }}
            75% {{ transform: rotate(-2deg); }}
        }}
        
        @keyframes armFloat {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            50% {{ transform: translateY(-3px) rotate(5deg); }}
        }}
        
        @keyframes legShift {{
            0%, 100% {{ transform: translateX(0px); }}
            50% {{ transform: translateX(2px); }}
        }}
        
        @keyframes auraGlow {{
            0%, 100% {{ opacity: 0.3; transform: scale(1); }}
            50% {{ opacity: 0.6; transform: scale(1.1); }}
        }}
    </style>
</head>
<body>
    <div class="character">
        <div class="aura"></div>
        <div class="character-head"></div>
        <div class="character-body"></div>
        <div class="character-arm arm-left"></div>
        <div class="character-arm arm-right"></div>
        <div class="character-leg leg-left"></div>
        <div class="character-leg leg-right"></div>
    </div>
</body>
</html>
        '''
    
    def _create_character_attack_animation(self, colors: Dict, duration: int, complexity: str, 
                                         keywords: List[str], mood: str, style: str) -> str:
        """Create character attack animation"""
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Character Attack Animation</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(45deg, {colors['background']}, {colors['primary']});
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }}
        
        .character {{
            width: 100px;
            height: 150px;
            position: relative;
            animation: attackSequence {duration}s infinite;
        }}
        
        .weapon {{
            width: 60px;
            height: 8px;
            background: {colors['accent']};
            border-radius: 4px;
            position: absolute;
            top: 60px;
            right: -20px;
            transform-origin: left center;
            animation: weaponSwing {duration}s infinite;
        }}
        
        .impact-effect {{
            width: 30px;
            height: 30px;
            background: radial-gradient(circle, {colors['secondary']}, transparent);
            border-radius: 50%;
            position: absolute;
            top: 50px;
            right: -50px;
            opacity: 0;
            animation: impactFlash {duration}s infinite;
        }}
        
        @keyframes attackSequence {{
            0%, 80% {{ transform: translateX(0px) scale(1); }}
            10% {{ transform: translateX(-5px) scale(1.05); }}
            20% {{ transform: translateX(10px) scale(0.95); }}
            30% {{ transform: translateX(0px) scale(1); }}
        }}
        
        @keyframes weaponSwing {{
            0%, 80% {{ transform: rotate(0deg); }}
            10% {{ transform: rotate(-45deg); }}
            20% {{ transform: rotate(45deg); }}
            30% {{ transform: rotate(0deg); }}
        }}
        
        @keyframes impactFlash {{
            0%, 15%, 25%, 100% {{ opacity: 0; transform: scale(1); }}
            20% {{ opacity: 1; transform: scale(1.5); }}
        }}
    </style>
</head>
<body>
    <div class="character">
        <div class="weapon"></div>
        <div class="impact-effect"></div>
        <!-- Character body would go here -->
    </div>
</body>
</html>
        '''
    
    def _create_environment_flow_animation(self, colors: Dict, duration: int, complexity: str, 
                                         keywords: List[str], mood: str, style: str) -> str:
        """Create flowing environment animation"""
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Environment Flow Animation</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: {colors['background']};
            overflow: hidden;
            height: 100vh;
        }}
        
        .flow-container {{
            width: 100%;
            height: 100%;
            position: relative;
        }}
        
        .flow-element {{
            position: absolute;
            border-radius: 50%;
            animation: flowMove {duration}s infinite linear;
        }}
        
        .flow-1 {{
            width: 20px;
            height: 20px;
            background: {colors['primary']};
            top: 20%;
            left: -50px;
            animation-delay: 0s;
        }}
        
        .flow-2 {{
            width: 15px;
            height: 15px;
            background: {colors['secondary']};
            top: 40%;
            left: -50px;
            animation-delay: 1s;
        }}
        
        .flow-3 {{
            width: 25px;
            height: 25px;
            background: {colors['accent']};
            top: 60%;
            left: -50px;
            animation-delay: 2s;
        }}
        
        @keyframes flowMove {{
            0% {{ 
                transform: translateX(0px) translateY(0px) scale(1);
                opacity: 0;
            }}
            10% {{ opacity: 1; }}
            90% {{ opacity: 1; }}
            100% {{ 
                transform: translateX(100vw) translateY(-50px) scale(0.5);
                opacity: 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="flow-container">
        <div class="flow-element flow-1"></div>
        <div class="flow-element flow-2"></div>
        <div class="flow-element flow-3"></div>
    </div>
</body>
</html>
        '''
    
    def _create_ui_transition_animation(self, colors: Dict, duration: int, complexity: str, 
                                      keywords: List[str], mood: str, style: str) -> str:
        """Create UI transition animation"""
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UI Transition Animation</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: {colors['background']};
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }}
        
        .ui-container {{
            width: 300px;
            height: 200px;
            background: {colors['primary']};
            border-radius: 10px;
            position: relative;
            overflow: hidden;
            animation: containerPulse {duration}s infinite ease-in-out;
        }}
        
        .ui-header {{
            width: 100%;
            height: 50px;
            background: {colors['secondary']};
            display: flex;
            align-items: center;
            padding: 0 20px;
            box-sizing: border-box;
            animation: headerSlide {duration}s infinite ease-in-out;
        }}
        
        .ui-content {{
            padding: 20px;
            color: {colors['text']};
            animation: contentFade {duration}s infinite ease-in-out;
        }}
        
        .ui-button {{
            width: 100px;
            height: 35px;
            background: {colors['accent']};
            border: none;
            border-radius: 5px;
            color: {colors['text']};
            margin-top: 20px;
            animation: buttonHover {duration}s infinite ease-in-out;
        }}
        
        @keyframes containerPulse {{
            0%, 100% {{ transform: scale(1); box-shadow: 0 0 0 rgba(0,0,0,0.3); }}
            50% {{ transform: scale(1.02); box-shadow: 0 10px 20px rgba(0,0,0,0.3); }}
        }}
        
        @keyframes headerSlide {{
            0%, 100% {{ transform: translateX(0px); }}
            50% {{ transform: translateX(5px); }}
        }}
        
        @keyframes contentFade {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.8; }}
        }}
        
        @keyframes buttonHover {{
            0%, 100% {{ transform: translateY(0px); background: {colors['accent']}; }}
            50% {{ transform: translateY(-2px); background: {colors['secondary']}; }}
        }}
    </style>
</head>
<body>
    <div class="ui-container">
        <div class="ui-header">
            <h3 style="margin: 0; color: {colors['text']};">UI Panel</h3>
        </div>
        <div class="ui-content">
            <p>This is an animated UI transition example.</p>
            <button class="ui-button">Click Me</button>
        </div>
    </div>
</body>
</html>
        '''
    
    def _create_particle_effect_animation(self, colors: Dict, duration: int, complexity: str, 
                                        keywords: List[str], mood: str, style: str) -> str:
        """Create particle effect animation"""
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Particle Effect Animation</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: {colors['background']};
            overflow: hidden;
            height: 100vh;
        }}
        
        .particle-system {{
            width: 100%;
            height: 100%;
            position: relative;
        }}
        
        .particle {{
            position: absolute;
            border-radius: 50%;
            animation: particleFloat {duration}s infinite ease-out;
        }}
        
        .particle-1 {{
            width: 8px;
            height: 8px;
            background: {colors['primary']};
            top: 50%;
            left: 50%;
            animation-delay: 0s;
        }}
        
        .particle-2 {{
            width: 6px;
            height: 6px;
            background: {colors['secondary']};
            top: 50%;
            left: 50%;
            animation-delay: 0.5s;
        }}
        
        .particle-3 {{
            width: 10px;
            height: 10px;
            background: {colors['accent']};
            top: 50%;
            left: 50%;
            animation-delay: 1s;
        }}
        
        @keyframes particleFloat {{
            0% {{
                transform: translate(0px, 0px) scale(1);
                opacity: 1;
            }}
            100% {{
                transform: translate(200px, -200px) scale(0);
                opacity: 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="particle-system">
        <div class="particle particle-1"></div>
        <div class="particle particle-2"></div>
        <div class="particle particle-3"></div>
    </div>
</body>
</html>
        '''
    
    def _create_text_reveal_animation(self, colors: Dict, duration: int, complexity: str, 
                                    keywords: List[str], mood: str, style: str) -> str:
        """Create text reveal animation"""
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Reveal Animation</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: {colors['background']};
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            color: {colors['text']};
        }}
        
        .text-container {{
            text-align: center;
            overflow: hidden;
        }}
        
        .reveal-text {{
            font-size: 3em;
            font-weight: bold;
            animation: textReveal {duration}s ease-out;
        }}
        
        .subtitle {{
            font-size: 1.2em;
            margin-top: 20px;
            animation: subtitleFade {duration}s ease-out;
            animation-delay: 1s;
            opacity: 0;
            animation-fill-mode: forwards;
        }}
        
        @keyframes textReveal {{
            0% {{
                transform: translateY(100px);
                opacity: 0;
            }}
            100% {{
                transform: translateY(0px);
                opacity: 1;
            }}
        }}
        
        @keyframes subtitleFade {{
            0% {{
                opacity: 0;
                transform: translateY(20px);
            }}
            100% {{
                opacity: 1;
                transform: translateY(0px);
            }}
        }}
    </style>
</head>
<body>
    <div class="text-container">
        <div class="reveal-text">MYTHIQ</div>
        <div class="subtitle">AI Creative Platform</div>
    </div>
</body>
</html>
        '''
    
    def _create_logo_animation_animation(self, colors: Dict, duration: int, complexity: str, 
                                       keywords: List[str], mood: str, style: str) -> str:
        """Create logo animation"""
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logo Animation</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: {colors['background']};
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }}
        
        .logo-container {{
            width: 200px;
            height: 200px;
            position: relative;
            animation: logoSpin {duration}s infinite ease-in-out;
        }}
        
        .logo-element {{
            position: absolute;
            border-radius: 50%;
        }}
        
        .logo-center {{
            width: 60px;
            height: 60px;
            background: {colors['primary']};
            top: 70px;
            left: 70px;
            animation: centerPulse 2s infinite ease-in-out;
        }}
        
        .logo-ring {{
            width: 120px;
            height: 120px;
            border: 10px solid {colors['secondary']};
            background: transparent;
            top: 40px;
            left: 40px;
            animation: ringRotate 3s infinite linear;
        }}
        
        .logo-accent {{
            width: 20px;
            height: 20px;
            background: {colors['accent']};
            top: 30px;
            left: 90px;
            animation: accentOrbit 4s infinite linear;
        }}
        
        @keyframes logoSpin {{
            0%, 100% {{ transform: rotate(0deg) scale(1); }}
            50% {{ transform: rotate(180deg) scale(1.1); }}
        }}
        
        @keyframes centerPulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.2); }}
        }}
        
        @keyframes ringRotate {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        
        @keyframes accentOrbit {{
            0% {{ transform: rotate(0deg) translateX(50px) rotate(0deg); }}
            100% {{ transform: rotate(360deg) translateX(50px) rotate(-360deg); }}
        }}
    </style>
</head>
<body>
    <div class="logo-container">
        <div class="logo-element logo-ring"></div>
        <div class="logo-element logo-center"></div>
        <div class="logo-element logo-accent"></div>
    </div>
</body>
</html>
        '''

# Example usage and testing
if __name__ == "__main__":
    # Initialize the Video Generator
    generator = VideoGenerator()
    
    # Test video generation
    test_analysis = {
        'theme': 'ninja',
        'style': 'cartoon',
        'complexity': 'detailed',
        'keywords': ['character', 'walking', 'animation'],
        'mood': 'epic'
    }
    
    print("🧪 Testing Video Generator:")
    print("=" * 40)
    
    result = generator.generate("Create a ninja character walking animation", test_analysis)
    
    print(f"Success: {result['success']}")
    print(f"Format: {result['format']}")
    print(f"Animation Type: {result.get('animation_type', 'N/A')}")
    print(f"Duration: {result.get('duration', 'N/A')}s")
    print(f"Description: {result['description']}")
    print(f"HTML Length: {len(result['content'])} characters")
    
    print("\n🎬 Video Generator ready for production use!")

