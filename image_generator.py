"""
Mythiq Image Generator - Advanced Procedural Image Generation
Creates professional-quality images using SVG, CSS, and mathematical generation
"""

import json
import math
import random
import colorsys
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class ImageGenerator:
    """
    Advanced image generation system using procedural techniques
    Creates SVG images with dynamic styling and animation
    """
    
    def __init__(self):
        """Initialize the image generation system"""
        self.color_schemes = {
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
        
        self.character_templates = {
            'humanoid': self._create_humanoid_template,
            'warrior': self._create_warrior_template,
            'mage': self._create_mage_template,
            'creature': self._create_creature_template,
            'robot': self._create_robot_template
        }
        
        self.environment_templates = {
            'landscape': self._create_landscape_template,
            'interior': self._create_interior_template,
            'abstract': self._create_abstract_template,
            'pattern': self._create_pattern_template,
            'ui_element': self._create_ui_template
        }
        
        print("🎨 Advanced Image Generator initialized with procedural capabilities")
    
    def generate(self, prompt: str, analysis: Dict) -> Dict:
        """
        Generate image based on prompt and analysis
        
        Args:
            prompt (str): User's image request
            analysis (Dict): AI analysis of the prompt
            
        Returns:
            Dict: Generated image data and metadata
        """
        theme = analysis.get('theme', 'default')
        style = analysis.get('style', 'default')
        complexity = analysis.get('complexity', 'medium')
        keywords = analysis.get('keywords', [])
        
        # Determine image type
        image_type = self._determine_image_type(keywords, prompt)
        
        # Generate the image
        if image_type == 'character':
            result = self._generate_character(prompt, theme, style, complexity, keywords)
        elif image_type == 'environment':
            result = self._generate_environment(prompt, theme, style, complexity, keywords)
        elif image_type == 'ui_element':
            result = self._generate_ui_element(prompt, theme, style, complexity, keywords)
        else:
            result = self._generate_abstract(prompt, theme, style, complexity, keywords)
        
        # Add metadata
        result.update({
            'generation_method': 'procedural_svg',
            'theme': theme,
            'style': style,
            'complexity': complexity,
            'image_type': image_type,
            'prompt': prompt,
            'timestamp': datetime.now().isoformat(),
            'generator_version': '3.0.0'
        })
        
        return result
    
    def _determine_image_type(self, keywords: List[str], prompt: str) -> str:
        """Determine what type of image to generate"""
        character_words = ['character', 'person', 'hero', 'warrior', 'ninja', 'mage', 'knight', 'robot', 'creature']
        environment_words = ['background', 'landscape', 'scene', 'environment', 'forest', 'castle', 'space', 'room']
        ui_words = ['button', 'icon', 'logo', 'interface', 'ui', 'menu', 'badge', 'symbol']
        
        if any(word in prompt.lower() for word in character_words):
            return 'character'
        elif any(word in prompt.lower() for word in environment_words):
            return 'environment'
        elif any(word in prompt.lower() for word in ui_words):
            return 'ui_element'
        else:
            return 'abstract'
    
    def _generate_character(self, prompt: str, theme: str, style: str, complexity: str, keywords: List[str]) -> Dict:
        """Generate character image"""
        colors = self.color_schemes.get(theme, self.color_schemes['default'])
        
        # Determine character type
        char_type = 'humanoid'
        if 'warrior' in keywords or 'knight' in keywords:
            char_type = 'warrior'
        elif 'mage' in keywords or 'wizard' in keywords:
            char_type = 'mage'
        elif 'robot' in keywords or 'android' in keywords:
            char_type = 'robot'
        elif 'creature' in keywords or 'monster' in keywords:
            char_type = 'creature'
        
        # Generate character SVG
        svg_content = self.character_templates[char_type](colors, complexity, keywords)
        
        return {
            'success': True,
            'format': 'svg',
            'content': svg_content,
            'character_type': char_type,
            'colors_used': colors,
            'description': f"Generated {char_type} character with {theme} theme",
            'usage_tips': [
                "SVG can be scaled to any size without quality loss",
                "Colors can be modified by editing the SVG code",
                "Animation elements are included for dynamic effects"
            ]
        }
    
    def _generate_environment(self, prompt: str, theme: str, style: str, complexity: str, keywords: List[str]) -> Dict:
        """Generate environment/background image"""
        colors = self.color_schemes.get(theme, self.color_schemes['default'])
        
        # Determine environment type
        env_type = 'landscape'
        if 'interior' in keywords or 'room' in keywords or 'indoor' in keywords:
            env_type = 'interior'
        elif 'abstract' in keywords or 'pattern' in keywords:
            env_type = 'abstract'
        
        # Generate environment SVG
        svg_content = self.environment_templates[env_type](colors, complexity, keywords, theme)
        
        return {
            'success': True,
            'format': 'svg',
            'content': svg_content,
            'environment_type': env_type,
            'colors_used': colors,
            'description': f"Generated {env_type} environment with {theme} theme",
            'usage_tips': [
                "Perfect for game backgrounds",
                "Can be used as website headers",
                "Includes subtle animations for dynamic feel"
            ]
        }
    
    def _generate_ui_element(self, prompt: str, theme: str, style: str, complexity: str, keywords: List[str]) -> Dict:
        """Generate UI element image"""
        colors = self.color_schemes.get(theme, self.color_schemes['default'])
        
        # Generate UI element SVG
        svg_content = self.environment_templates['ui_element'](colors, complexity, keywords)
        
        return {
            'success': True,
            'format': 'svg',
            'content': svg_content,
            'element_type': 'ui_component',
            'colors_used': colors,
            'description': f"Generated UI element with {theme} theme",
            'usage_tips': [
                "Ready for web and app interfaces",
                "Scalable vector format",
                "Hover effects included"
            ]
        }
    
    def _generate_abstract(self, prompt: str, theme: str, style: str, complexity: str, keywords: List[str]) -> Dict:
        """Generate abstract art image"""
        colors = self.color_schemes.get(theme, self.color_schemes['default'])
        
        # Generate abstract SVG
        svg_content = self.environment_templates['abstract'](colors, complexity, keywords)
        
        return {
            'success': True,
            'format': 'svg',
            'content': svg_content,
            'art_type': 'abstract',
            'colors_used': colors,
            'description': f"Generated abstract art with {theme} theme",
            'usage_tips': [
                "Great for artistic backgrounds",
                "Can be used as decorative elements",
                "Includes mathematical precision"
            ]
        }
    
    def _create_humanoid_template(self, colors: Dict, complexity: str, keywords: List[str]) -> str:
        """Create humanoid character template"""
        width, height = 200, 300
        
        # Add complexity-based details
        details = ""
        if complexity in ['detailed', 'professional']:
            details = f'''
            <!-- Detailed armor/clothing -->
            <rect x="75" y="125" width="50" height="20" fill="{colors['accent']}" rx="3" opacity="0.8"/>
            <circle cx="85" cy="135" r="3" fill="{colors['secondary']}"/>
            <circle cx="115" cy="135" r="3" fill="{colors['secondary']}"/>
            
            <!-- Belt -->
            <rect x="70" y="160" width="60" height="8" fill="{colors['secondary']}" rx="2"/>
            <rect x="95" y="158" width="10" height="12" fill="{colors['accent']}" rx="1"/>
            '''
        
        # Add theme-specific elements
        theme_elements = ""
        if 'ninja' in keywords:
            theme_elements = f'''
            <!-- Ninja mask -->
            <path d="M 85 65 Q 100 60 115 65 Q 115 85 100 85 Q 85 85 85 65" fill="{colors['primary']}"/>
            <circle cx="92" cy="75" r="2" fill="{colors['accent']}"/>
            <circle cx="108" cy="75" r="2" fill="{colors['accent']}"/>
            
            <!-- Ninja weapon -->
            <line x1="45" y1="130" x2="25" y2="110" stroke="{colors['accent']}" stroke-width="3"/>
            <circle cx="25" cy="110" r="4" fill="{colors['secondary']}"/>
            '''
        
        return f'''
        <svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="bodyGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:{colors['primary']};stop-opacity:1" />
                    <stop offset="100%" style="stop-color:{colors['secondary']};stop-opacity:0.8" />
                </linearGradient>
                <radialGradient id="glowEffect" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" style="stop-color:{colors['accent']};stop-opacity:0.6" />
                    <stop offset="100%" style="stop-color:{colors['accent']};stop-opacity:0" />
                </radialGradient>
            </defs>
            
            <!-- Glow effect -->
            <ellipse cx="100" cy="150" rx="80" ry="120" fill="url(#glowEffect)"/>
            
            <!-- Head -->
            <ellipse cx="100" cy="80" rx="30" ry="35" fill="url(#bodyGradient)"/>
            
            <!-- Body -->
            <rect x="80" y="110" width="40" height="80" fill="{colors['primary']}" rx="5"/>
            
            <!-- Arms -->
            <ellipse cx="60" cy="140" rx="12" ry="30" fill="{colors['primary']}" transform="rotate(-10 60 140)"/>
            <ellipse cx="140" cy="140" rx="12" ry="30" fill="{colors['primary']}" transform="rotate(10 140 140)"/>
            
            <!-- Legs -->
            <ellipse cx="85" cy="210" rx="12" ry="35" fill="{colors['primary']}"/>
            <ellipse cx="115" cy="210" rx="12" ry="35" fill="{colors['primary']}"/>
            
            <!-- Eyes -->
            <circle cx="90" cy="75" r="3" fill="{colors['accent']}"/>
            <circle cx="110" cy="75" r="3" fill="{colors['accent']}"/>
            
            {details}
            {theme_elements}
            
            <!-- Animation -->
            <animateTransform attributeName="transform" type="rotate" 
                             values="0 100 150;1 100 150;-1 100 150;0 100 150" 
                             dur="4s" repeatCount="indefinite"/>
        </svg>
        '''
    
    def _create_warrior_template(self, colors: Dict, complexity: str, keywords: List[str]) -> str:
        """Create warrior character template"""
        return f'''
        <svg width="220" height="320" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="armorGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:{colors['secondary']};stop-opacity:1" />
                    <stop offset="50%" style="stop-color:{colors['primary']};stop-opacity:1" />
                    <stop offset="100%" style="stop-color:{colors['accent']};stop-opacity:1" />
                </linearGradient>
            </defs>
            
            <!-- Warrior silhouette -->
            <ellipse cx="110" cy="80" rx="35" ry="40" fill="url(#armorGradient)"/>
            
            <!-- Armored body -->
            <rect x="85" y="115" width="50" height="90" fill="{colors['primary']}" rx="8"/>
            <rect x="80" y="120" width="60" height="15" fill="{colors['secondary']}" rx="3"/>
            <rect x="80" y="140" width="60" height="15" fill="{colors['secondary']}" rx="3"/>
            
            <!-- Shield -->
            <ellipse cx="50" cy="150" rx="20" ry="35" fill="{colors['accent']}" transform="rotate(-15 50 150)"/>
            <circle cx="50" cy="150" r="8" fill="{colors['secondary']}"/>
            
            <!-- Sword -->
            <rect x="165" y="120" width="6" height="60" fill="{colors['accent']}"/>
            <rect x="160" y="115" width="16" height="8" fill="{colors['secondary']}"/>
            <circle cx="168" cy="110" r="5" fill="{colors['primary']}"/>
            
            <!-- Helmet -->
            <path d="M 85 60 Q 110 45 135 60 Q 135 85 110 90 Q 85 85 85 60" fill="{colors['secondary']}"/>
            <rect x="105" y="50" width="10" height="25" fill="{colors['accent']}"/>
            
            <!-- Legs with armor -->
            <ellipse cx="90" cy="230" rx="15" ry="40" fill="{colors['primary']}"/>
            <ellipse cx="130" cy="230" rx="15" ry="40" fill="{colors['primary']}"/>
            <rect x="82" y="210" width="16" height="12" fill="{colors['secondary']}" rx="2"/>
            <rect x="122" y="210" width="16" height="12" fill="{colors['secondary']}" rx="2"/>
            
            <!-- Battle stance animation -->
            <animateTransform attributeName="transform" type="rotate" 
                             values="0 110 160;2 110 160;-1 110 160;0 110 160" 
                             dur="3s" repeatCount="indefinite"/>
        </svg>
        '''
    
    def _create_mage_template(self, colors: Dict, complexity: str, keywords: List[str]) -> str:
        """Create mage character template"""
        return f'''
        <svg width="200" height="350" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <radialGradient id="magicGlow" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" style="stop-color:{colors['accent']};stop-opacity:0.8" />
                    <stop offset="100%" style="stop-color:{colors['accent']};stop-opacity:0" />
                </radialGradient>
                <linearGradient id="robeGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:{colors['primary']};stop-opacity:1" />
                    <stop offset="100%" style="stop-color:{colors['secondary']};stop-opacity:1" />
                </linearGradient>
            </defs>
            
            <!-- Magic aura -->
            <circle cx="100" cy="175" r="90" fill="url(#magicGlow)"/>
            
            <!-- Robe -->
            <path d="M 70 120 Q 100 115 130 120 Q 140 200 130 280 Q 100 290 70 280 Q 60 200 70 120" fill="url(#robeGradient)"/>
            
            <!-- Head -->
            <circle cx="100" cy="80" r="25" fill="{colors['background']}"/>
            
            <!-- Wizard hat -->
            <path d="M 80 65 Q 100 30 120 65 Q 110 70 100 75 Q 90 70 80 65" fill="{colors['primary']}"/>
            <circle cx="100" cy="35" r="4" fill="{colors['accent']}"/>
            
            <!-- Staff -->
            <line x1="40" y1="100" x2="40" y2="250" stroke="{colors['secondary']}" stroke-width="4"/>
            <circle cx="40" cy="95" r="8" fill="{colors['accent']}">
                <animate attributeName="fill" values="{colors['accent']};{colors['secondary']};{colors['accent']}" dur="2s" repeatCount="indefinite"/>
            </circle>
            
            <!-- Magic orbs -->
            <circle cx="160" cy="140" r="6" fill="{colors['accent']}" opacity="0.7">
                <animate attributeName="cy" values="140;120;140" dur="3s" repeatCount="indefinite"/>
                <animate attributeName="opacity" values="0.7;1;0.7" dur="3s" repeatCount="indefinite"/>
            </circle>
            <circle cx="170" cy="160" r="4" fill="{colors['secondary']}" opacity="0.5">
                <animate attributeName="cy" values="160;140;160" dur="2.5s" repeatCount="indefinite"/>
            </circle>
            
            <!-- Eyes with magic glow -->
            <circle cx="92" cy="78" r="2" fill="{colors['accent']}"/>
            <circle cx="108" cy="78" r="2" fill="{colors['accent']}"/>
            
            <!-- Floating animation -->
            <animateTransform attributeName="transform" type="translate" 
                             values="0 0;0 -5;0 0" 
                             dur="4s" repeatCount="indefinite"/>
        </svg>
        '''
    
    def _create_creature_template(self, colors: Dict, complexity: str, keywords: List[str]) -> str:
        """Create creature character template"""
        return f'''
        <svg width="250" height="280" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <radialGradient id="creatureBody" cx="30%" cy="30%" r="70%">
                    <stop offset="0%" style="stop-color:{colors['accent']};stop-opacity:1" />
                    <stop offset="70%" style="stop-color:{colors['primary']};stop-opacity:1" />
                    <stop offset="100%" style="stop-color:{colors['secondary']};stop-opacity:1" />
                </radialGradient>
            </defs>
            
            <!-- Main body -->
            <ellipse cx="125" cy="140" rx="60" ry="80" fill="url(#creatureBody)"/>
            
            <!-- Head -->
            <ellipse cx="125" cy="80" rx="40" ry="35" fill="{colors['primary']}"/>
            
            <!-- Horns/Spikes -->
            <polygon points="105,50 110,70 100,70" fill="{colors['secondary']}"/>
            <polygon points="145,50 150,70 140,70" fill="{colors['secondary']}"/>
            <polygon points="125,45 130,65 120,65" fill="{colors['accent']}"/>
            
            <!-- Eyes -->
            <ellipse cx="115" cy="75" rx="6" ry="8" fill="{colors['accent']}">
                <animate attributeName="fill" values="{colors['accent']};{colors['secondary']};{colors['accent']}" dur="3s" repeatCount="indefinite"/>
            </ellipse>
            <ellipse cx="135" cy="75" rx="6" ry="8" fill="{colors['accent']}">
                <animate attributeName="fill" values="{colors['accent']};{colors['secondary']};{colors['accent']}" dur="3s" repeatCount="indefinite"/>
            </ellipse>
            
            <!-- Claws/Arms -->
            <ellipse cx="70" cy="120" rx="15" ry="40" fill="{colors['primary']}" transform="rotate(-30 70 120)"/>
            <ellipse cx="180" cy="120" rx="15" ry="40" fill="{colors['primary']}" transform="rotate(30 180 120)"/>
            
            <!-- Claws -->
            <polygon points="55,100 60,110 50,115" fill="{colors['secondary']}"/>
            <polygon points="50,105 55,115 45,120" fill="{colors['secondary']}"/>
            <polygon points="195,100 200,110 190,115" fill="{colors['secondary']}"/>
            <polygon points="200,105 205,115 195,120" fill="{colors['secondary']}"/>
            
            <!-- Legs -->
            <ellipse cx="100" cy="200" rx="18" ry="35" fill="{colors['primary']}"/>
            <ellipse cx="150" cy="200" rx="18" ry="35" fill="{colors['primary']}"/>
            
            <!-- Tail -->
            <path d="M 125 220 Q 160 240 180 260 Q 185 265 180 270 Q 155 250 125 230" fill="{colors['secondary']}"/>
            
            <!-- Breathing animation -->
            <animateTransform attributeName="transform" type="scale" 
                             values="1;1.05;1" 
                             dur="3s" repeatCount="indefinite"/>
        </svg>
        '''
    
    def _create_robot_template(self, colors: Dict, complexity: str, keywords: List[str]) -> str:
        """Create robot character template"""
        return f'''
        <svg width="200" height="300" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="metalGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:{colors['accent']};stop-opacity:1" />
                    <stop offset="50%" style="stop-color:{colors['primary']};stop-opacity:1" />
                    <stop offset="100%" style="stop-color:{colors['secondary']};stop-opacity:1" />
                </linearGradient>
            </defs>
            
            <!-- Head -->
            <rect x="75" y="60" width="50" height="40" fill="url(#metalGradient)" rx="5"/>
            
            <!-- Eyes -->
            <circle cx="85" cy="75" r="5" fill="{colors['accent']}">
                <animate attributeName="fill" values="{colors['accent']};{colors['secondary']};{colors['accent']}" dur="2s" repeatCount="indefinite"/>
            </circle>
            <circle cx="115" cy="75" r="5" fill="{colors['accent']}">
                <animate attributeName="fill" values="{colors['accent']};{colors['secondary']};{colors['accent']}" dur="2s" repeatCount="indefinite"/>
            </circle>
            
            <!-- Antenna -->
            <line x1="100" y1="60" x2="100" y2="45" stroke="{colors['secondary']}" stroke-width="2"/>
            <circle cx="100" cy="45" r="3" fill="{colors['accent']}">
                <animate attributeName="fill" values="{colors['accent']};{colors['primary']};{colors['accent']}" dur="1s" repeatCount="indefinite"/>
            </circle>
            
            <!-- Body -->
            <rect x="80" y="100" width="40" height="70" fill="{colors['primary']}" rx="3"/>
            
            <!-- Chest panel -->
            <rect x="85" y="110" width="30" height="20" fill="{colors['secondary']}" rx="2"/>
            <circle cx="90" cy="120" r="2" fill="{colors['accent']}"/>
            <circle cx="100" cy="120" r="2" fill="{colors['accent']}"/>
            <circle cx="110" cy="120" r="2" fill="{colors['accent']}"/>
            
            <!-- Arms -->
            <rect x="55" y="110" width="15" height="40" fill="{colors['primary']}" rx="3"/>
            <rect x="130" y="110" width="15" height="40" fill="{colors['primary']}" rx="3"/>
            
            <!-- Joints -->
            <circle cx="62" cy="130" r="4" fill="{colors['secondary']}"/>
            <circle cx="138" cy="130" r="4" fill="{colors['secondary']}"/>
            
            <!-- Legs -->
            <rect x="85" y="170" width="12" height="50" fill="{colors['primary']}" rx="2"/>
            <rect x="103" y="170" width="12" height="50" fill="{colors['primary']}" rx="2"/>
            
            <!-- Feet -->
            <rect x="80" y="220" width="20" height="8" fill="{colors['secondary']}" rx="2"/>
            <rect x="100" y="220" width="20" height="8" fill="{colors['secondary']}" rx="2"/>
            
            <!-- Power indicator -->
            <rect x="88" y="140" width="24" height="4" fill="{colors['background']}" rx="1"/>
            <rect x="90" y="141" width="20" height="2" fill="{colors['accent']}" rx="1">
                <animate attributeName="width" values="20;5;20" dur="3s" repeatCount="indefinite"/>
            </rect>
            
            <!-- Mechanical movement -->
            <animateTransform attributeName="transform" type="rotate" 
                             values="0 100 150;1 100 150;-1 100 150;0 100 150" 
                             dur="2s" repeatCount="indefinite"/>
        </svg>
        '''
    
    def _create_landscape_template(self, colors: Dict, complexity: str, keywords: List[str], theme: str) -> str:
        """Create landscape environment template"""
        width, height = 400, 250
        
        # Theme-specific landscape elements
        if theme == 'space':
            return self._create_space_landscape(colors, width, height, complexity)
        elif theme == 'forest':
            return self._create_forest_landscape(colors, width, height, complexity)
        elif theme == 'medieval':
            return self._create_medieval_landscape(colors, width, height, complexity)
        else:
            return self._create_default_landscape(colors, width, height, complexity)
    
    def _create_space_landscape(self, colors: Dict, width: int, height: int, complexity: str) -> str:
        """Create space-themed landscape"""
        return f'''
        <svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <radialGradient id="spaceGradient" cx="50%" cy="0%" r="100%">
                    <stop offset="0%" style="stop-color:{colors['secondary']};stop-opacity:0.3" />
                    <stop offset="100%" style="stop-color:{colors['background']};stop-opacity:1" />
                </radialGradient>
            </defs>
            
            <!-- Space background -->
            <rect width="{width}" height="{height}" fill="url(#spaceGradient)"/>
            
            <!-- Stars -->
            <circle cx="50" cy="30" r="1" fill="{colors['accent']}" opacity="0.8">
                <animate attributeName="opacity" values="0.8;1;0.8" dur="2s" repeatCount="indefinite"/>
            </circle>
            <circle cx="150" cy="50" r="1.5" fill="{colors['accent']}" opacity="0.6">
                <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" repeatCount="indefinite"/>
            </circle>
            <circle cx="300" cy="40" r="1" fill="{colors['accent']}" opacity="0.9">
                <animate attributeName="opacity" values="0.9;0.5;0.9" dur="2.5s" repeatCount="indefinite"/>
            </circle>
            <circle cx="350" cy="70" r="2" fill="{colors['secondary']}" opacity="0.7">
                <animate attributeName="opacity" values="0.7;1;0.7" dur="4s" repeatCount="indefinite"/>
            </circle>
            
            <!-- Planets -->
            <circle cx="320" cy="80" r="25" fill="{colors['primary']}" opacity="0.8"/>
            <circle cx="320" cy="80" r="20" fill="{colors['secondary']}" opacity="0.4"/>
            
            <!-- Nebula -->
            <ellipse cx="100" cy="100" rx="60" ry="30" fill="{colors['accent']}" opacity="0.2">
                <animate attributeName="opacity" values="0.2;0.4;0.2" dur="8s" repeatCount="indefinite"/>
            </ellipse>
            
            <!-- Asteroid field -->
            <circle cx="200" cy="150" r="3" fill="{colors['primary']}">
                <animateTransform attributeName="transform" type="rotate" 
                                 values="0 200 150;360 200 150" dur="10s" repeatCount="indefinite"/>
            </circle>
            <circle cx="250" cy="180" r="2" fill="{colors['secondary']}">
                <animateTransform attributeName="transform" type="rotate" 
                                 values="0 250 180;-360 250 180" dur="15s" repeatCount="indefinite"/>
            </circle>
            
            <!-- Spaceship silhouette -->
            <polygon points="50,200 70,190 90,200 85,210 55,210" fill="{colors['accent']}" opacity="0.6">
                <animate attributeName="opacity" values="0.6;0.8;0.6" dur="3s" repeatCount="indefinite"/>
            </polygon>
        </svg>
        '''
    
    def _create_forest_landscape(self, colors: Dict, width: int, height: int, complexity: str) -> str:
        """Create forest-themed landscape"""
        return f'''
        <svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="forestSky" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:{colors['accent']};stop-opacity:0.6" />
                    <stop offset="100%" style="stop-color:{colors['primary']};stop-opacity:1" />
                </linearGradient>
            </defs>
            
            <!-- Sky -->
            <rect width="{width}" height="150" fill="url(#forestSky)"/>
            
            <!-- Ground -->
            <rect y="150" width="{width}" height="100" fill="{colors['secondary']}"/>
            
            <!-- Trees -->
            <ellipse cx="80" cy="120" rx="25" ry="40" fill="{colors['primary']}"/>
            <rect x="75" y="140" width="10" height="30" fill="{colors['background']}"/>
            
            <ellipse cx="200" cy="110" rx="30" ry="50" fill="{colors['primary']}"/>
            <rect x="195" y="135" width="10" height="35" fill="{colors['background']}"/>
            
            <ellipse cx="320" cy="125" rx="20" ry="35" fill="{colors['primary']}"/>
            <rect x="315" y="145" width="10" height="25" fill="{colors['background']}"/>
            
            <!-- Animated leaves -->
            <circle cx="90" cy="100" r="3" fill="{colors['accent']}">
                <animate attributeName="cy" values="100;120;100" dur="4s" repeatCount="indefinite"/>
                <animate attributeName="opacity" values="1;0.5;1" dur="4s" repeatCount="indefinite"/>
            </circle>
            <circle cx="210" cy="90" r="2" fill="{colors['accent']}">
                <animate attributeName="cy" values="90;110;90" dur="5s" repeatCount="indefinite"/>
            </circle>
            
            <!-- Sun rays -->
            <line x1="350" y1="30" x2="330" y2="50" stroke="{colors['accent']}" stroke-width="2" opacity="0.7">
                <animate attributeName="opacity" values="0.7;0.3;0.7" dur="3s" repeatCount="indefinite"/>
            </line>
            <line x1="370" y1="50" x2="350" y2="70" stroke="{colors['accent']}" stroke-width="2" opacity="0.5">
                <animate attributeName="opacity" values="0.5;0.8;0.5" dur="4s" repeatCount="indefinite"/>
            </line>
        </svg>
        '''
    
    def _create_medieval_landscape(self, colors: Dict, width: int, height: int, complexity: str) -> str:
        """Create medieval-themed landscape"""
        return f'''
        <svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
            <!-- Castle silhouette -->
            <rect x="150" y="80" width="100" height="80" fill="{colors['primary']}"/>
            <rect x="140" y="70" width="20" height="90" fill="{colors['primary']}"/>
            <rect x="240" y="70" width="20" height="90" fill="{colors['primary']}"/>
            <rect x="190" y="60" width="20" height="100" fill="{colors['primary']}"/>
            
            <!-- Castle flags -->
            <polygon points="150,70 160,70 155,80" fill="{colors['secondary']}">
                <animate attributeName="points" values="150,70 160,70 155,80;150,70 160,70 158,78;150,70 160,70 155,80" dur="2s" repeatCount="indefinite"/>
            </polygon>
            <polygon points="250,70 260,70 255,80" fill="{colors['accent']}">
                <animate attributeName="points" values="250,70 260,70 255,80;250,70 260,70 252,78;250,70 260,70 255,80" dur="2.5s" repeatCount="indefinite"/>
            </polygon>
            
            <!-- Mountains -->
            <polygon points="0,120 80,60 160,120 0,250 0,120" fill="{colors['background']}" opacity="0.7"/>
            <polygon points="240,120 320,70 400,120 400,250 240,250" fill="{colors['background']}" opacity="0.7"/>
            
            <!-- Ground -->
            <rect y="160" width="{width}" height="90" fill="{colors['secondary']}"/>
            
            <!-- Path -->
            <path d="M 0 200 Q 200 190 400 200" stroke="{colors['accent']}" stroke-width="8" fill="none" opacity="0.6"/>
        </svg>
        '''
    
    def _create_default_landscape(self, colors: Dict, width: int, height: int, complexity: str) -> str:
        """Create default landscape"""
        return f'''
        <svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="skyGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:{colors['accent']};stop-opacity:0.8" />
                    <stop offset="100%" style="stop-color:{colors['primary']};stop-opacity:1" />
                </linearGradient>
            </defs>
            
            <!-- Sky -->
            <rect width="{width}" height="180" fill="url(#skyGradient)"/>
            
            <!-- Sun -->
            <circle cx="320" cy="60" r="25" fill="{colors['secondary']}" opacity="0.8">
                <animate attributeName="cy" values="60;55;60" dur="4s" repeatCount="indefinite"/>
            </circle>
            
            <!-- Hills -->
            <ellipse cx="100" cy="160" rx="80" ry="40" fill="{colors['primary']}"/>
            <ellipse cx="300" cy="170" rx="100" ry="50" fill="{colors['secondary']}" opacity="0.8"/>
            
            <!-- Ground -->
            <rect y="180" width="{width}" height="70" fill="{colors['background']}"/>
        </svg>
        '''
    
    def _create_interior_template(self, colors: Dict, complexity: str, keywords: List[str]) -> str:
        """Create interior environment template"""
        return f'''
        <svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
            <!-- Room background -->
            <rect width="400" height="300" fill="{colors['background']}"/>
            
            <!-- Floor -->
            <rect y="250" width="400" height="50" fill="{colors['secondary']}" opacity="0.6"/>
            
            <!-- Wall panels -->
            <rect x="50" y="50" width="300" height="200" fill="{colors['primary']}" opacity="0.3"/>
            
            <!-- Window -->
            <rect x="150" y="80" width="100" height="80" fill="{colors['accent']}" opacity="0.4"/>
            <line x1="200" y1="80" x2="200" y2="160" stroke="{colors['secondary']}" stroke-width="2"/>
            <line x1="150" y1="120" x2="250" y2="120" stroke="{colors['secondary']}" stroke-width="2"/>
            
            <!-- Furniture silhouettes -->
            <rect x="80" y="200" width="60" height="50" fill="{colors['primary']}" opacity="0.7"/>
            <rect x="280" y="180" width="40" height="70" fill="{colors['primary']}" opacity="0.7"/>
        </svg>
        '''
    
    def _create_abstract_template(self, colors: Dict, complexity: str, keywords: List[str]) -> str:
        """Create abstract art template"""
        return f'''
        <svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <radialGradient id="abstractCenter" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" style="stop-color:{colors['accent']};stop-opacity:1" />
                    <stop offset="50%" style="stop-color:{colors['secondary']};stop-opacity:0.8" />
                    <stop offset="100%" style="stop-color:{colors['primary']};stop-opacity:1" />
                </radialGradient>
            </defs>
            
            <!-- Background -->
            <rect width="300" height="300" fill="url(#abstractCenter)"/>
            
            <!-- Geometric shapes -->
            <polygon points="150,50 200,100 150,150 100,100" fill="{colors['primary']}" opacity="0.8">
                <animateTransform attributeName="transform" type="rotate" 
                                 values="0 150 100;360 150 100" dur="10s" repeatCount="indefinite"/>
            </polygon>
            
            <circle cx="150" cy="150" r="40" fill="{colors['secondary']}" opacity="0.6">
                <animate attributeName="r" values="40;50;40" dur="3s" repeatCount="indefinite"/>
            </circle>
            
            <!-- Flowing lines -->
            <path d="M 50 150 Q 150 100 250 150 Q 150 200 50 150" stroke="{colors['accent']}" stroke-width="3" fill="none" opacity="0.8">
                <animate attributeName="stroke-width" values="3;6;3" dur="4s" repeatCount="indefinite"/>
            </path>
        </svg>
        '''
    
    def _create_pattern_template(self, colors: Dict, complexity: str, keywords: List[str]) -> str:
        """Create pattern template"""
        return f'''
        <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <pattern id="geometricPattern" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse">
                    <rect width="40" height="40" fill="{colors['primary']}"/>
                    <circle cx="20" cy="20" r="15" fill="{colors['secondary']}" opacity="0.7"/>
                    <rect x="15" y="15" width="10" height="10" fill="{colors['accent']}"/>
                </pattern>
            </defs>
            
            <rect width="200" height="200" fill="url(#geometricPattern)"/>
        </svg>
        '''
    
    def _create_ui_template(self, colors: Dict, complexity: str, keywords: List[str]) -> str:
        """Create UI element template"""
        if 'button' in keywords:
            return self._create_button_ui(colors, complexity)
        elif 'icon' in keywords:
            return self._create_icon_ui(colors, complexity)
        else:
            return self._create_generic_ui(colors, complexity)
    
    def _create_button_ui(self, colors: Dict, complexity: str) -> str:
        """Create button UI element"""
        return f'''
        <svg width="200" height="60" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="buttonGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:{colors['secondary']};stop-opacity:1" />
                    <stop offset="100%" style="stop-color:{colors['primary']};stop-opacity:1" />
                </linearGradient>
            </defs>
            
            <rect width="200" height="60" fill="url(#buttonGradient)" rx="10">
                <animate attributeName="fill" values="url(#buttonGradient);{colors['accent']};url(#buttonGradient)" dur="3s" repeatCount="indefinite"/>
            </rect>
            <text x="100" y="35" text-anchor="middle" fill="{colors['text']}" font-family="Arial" font-size="16" font-weight="bold">Click Me</text>
        </svg>
        '''
    
    def _create_icon_ui(self, colors: Dict, complexity: str) -> str:
        """Create icon UI element"""
        return f'''
        <svg width="64" height="64" xmlns="http://www.w3.org/2000/svg">
            <circle cx="32" cy="32" r="30" fill="{colors['primary']}" stroke="{colors['secondary']}" stroke-width="2"/>
            <polygon points="32,16 40,28 32,24 24,28" fill="{colors['accent']}"/>
            <rect x="28" y="28" width="8" height="20" fill="{colors['accent']}"/>
        </svg>
        '''
    
    def _create_generic_ui(self, colors: Dict, complexity: str) -> str:
        """Create generic UI element"""
        return f'''
        <svg width="150" height="100" xmlns="http://www.w3.org/2000/svg">
            <rect width="150" height="100" fill="{colors['background']}" stroke="{colors['primary']}" stroke-width="2" rx="5"/>
            <rect x="10" y="10" width="130" height="20" fill="{colors['secondary']}" rx="2"/>
            <circle cx="20" cy="50" r="8" fill="{colors['accent']}"/>
            <rect x="35" y="45" width="100" height="10" fill="{colors['primary']}" rx="1"/>
        </svg>
        '''

# Example usage and testing
if __name__ == "__main__":
    # Initialize the Image Generator
    generator = ImageGenerator()
    
    # Test image generation
    test_analysis = {
        'theme': 'ninja',
        'style': 'cartoon',
        'complexity': 'detailed',
        'keywords': ['character', 'warrior', 'stealth']
    }
    
    print("🧪 Testing Image Generator:")
    print("=" * 40)
    
    result = generator.generate("Create a ninja warrior character", test_analysis)
    
    print(f"Success: {result['success']}")
    print(f"Format: {result['format']}")
    print(f"Character Type: {result.get('character_type', 'N/A')}")
    print(f"Description: {result['description']}")
    print(f"SVG Length: {len(result['content'])} characters")
    
    print("\n🎨 Image Generator ready for production use!")

