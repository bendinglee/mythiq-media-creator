"""
Mythiq Template Manager - Advanced Asset Management System
Manages templates, themes, and assets for media generation
"""

import json
import os
import base64
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class TemplateManager:
    """
    Advanced template management system for media generation
    Handles themes, assets, templates, and customization options
    """
    
    def __init__(self):
        """Initialize the template management system"""
        self.themes = {
            'ninja': {
                'colors': {
                    'primary': '#2C3E50',
                    'secondary': '#E74C3C',
                    'accent': '#F39C12',
                    'background': '#34495E',
                    'text': '#ECF0F1'
                },
                'fonts': ['Arial Black', 'Impact', 'sans-serif'],
                'style': 'dark_stealth',
                'mood': 'mysterious',
                'elements': ['shadows', 'sharp_edges', 'minimal_lighting']
            },
            'space': {
                'colors': {
                    'primary': '#2980B9',
                    'secondary': '#8E44AD',
                    'accent': '#F1C40F',
                    'background': '#1A1A2E',
                    'text': '#FFFFFF'
                },
                'fonts': ['Orbitron', 'Roboto', 'monospace'],
                'style': 'futuristic',
                'mood': 'epic',
                'elements': ['gradients', 'glow_effects', 'geometric_shapes']
            },
            'medieval': {
                'colors': {
                    'primary': '#8B4513',
                    'secondary': '#DAA520',
                    'accent': '#CD853F',
                    'background': '#2F1B14',
                    'text': '#F5DEB3'
                },
                'fonts': ['Cinzel', 'serif'],
                'style': 'ancient',
                'mood': 'heroic',
                'elements': ['textures', 'ornate_borders', 'warm_lighting']
            },
            'forest': {
                'colors': {
                    'primary': '#27AE60',
                    'secondary': '#2ECC71',
                    'accent': '#F39C12',
                    'background': '#1E8449',
                    'text': '#FFFFFF'
                },
                'fonts': ['Verdana', 'sans-serif'],
                'style': 'natural',
                'mood': 'peaceful',
                'elements': ['organic_shapes', 'soft_shadows', 'natural_textures']
            },
            'underwater': {
                'colors': {
                    'primary': '#3498DB',
                    'secondary': '#5DADE2',
                    'accent': '#1ABC9C',
                    'background': '#154360',
                    'text': '#EBF5FB'
                },
                'fonts': ['Trebuchet MS', 'sans-serif'],
                'style': 'flowing',
                'mood': 'calm',
                'elements': ['wave_patterns', 'bubble_effects', 'fluid_motion']
            }
        }
        
        self.media_templates = {
            'character': {
                'svg_base': self._get_character_svg_template(),
                'customizable_parts': ['head', 'body', 'arms', 'legs', 'accessories'],
                'animation_options': ['idle', 'walk', 'jump', 'attack'],
                'size_variants': ['small', 'medium', 'large']
            },
            'environment': {
                'svg_base': self._get_environment_svg_template(),
                'customizable_parts': ['background', 'foreground', 'objects', 'effects'],
                'animation_options': ['static', 'parallax', 'dynamic'],
                'size_variants': ['thumbnail', 'standard', 'wallpaper']
            },
            'ui_element': {
                'svg_base': self._get_ui_element_svg_template(),
                'customizable_parts': ['shape', 'text', 'icon', 'border'],
                'animation_options': ['hover', 'click', 'pulse'],
                'size_variants': ['icon', 'button', 'panel']
            },
            'effect': {
                'svg_base': self._get_effect_svg_template(),
                'customizable_parts': ['particles', 'glow', 'trail', 'burst'],
                'animation_options': ['loop', 'trigger', 'sequence'],
                'size_variants': ['small', 'medium', 'large']
            }
        }
        
        self.style_presets = {
            'cartoon': {
                'stroke_width': 3,
                'corner_radius': 8,
                'shadow_blur': 5,
                'color_saturation': 1.2
            },
            'realistic': {
                'stroke_width': 1,
                'corner_radius': 2,
                'shadow_blur': 10,
                'color_saturation': 0.9
            },
            'minimalist': {
                'stroke_width': 2,
                'corner_radius': 0,
                'shadow_blur': 0,
                'color_saturation': 0.8
            },
            'fantasy': {
                'stroke_width': 2,
                'corner_radius': 5,
                'shadow_blur': 8,
                'color_saturation': 1.1
            }
        }
        
        print("🎨 Advanced Template Manager initialized with comprehensive asset system")
    
    def get_theme(self, theme_name: str) -> Dict:
        """Get theme configuration"""
        return self.themes.get(theme_name, self.themes['ninja'])
    
    def get_template(self, template_type: str) -> Dict:
        """Get media template configuration"""
        return self.media_templates.get(template_type, self.media_templates['character'])
    
    def get_style_preset(self, style_name: str) -> Dict:
        """Get style preset configuration"""
        return self.style_presets.get(style_name, self.style_presets['cartoon'])
    
    def customize_template(self, template_type: str, theme: str, style: str, 
                          customizations: Dict) -> Dict:
        """
        Customize a template with theme, style, and specific customizations
        
        Args:
            template_type (str): Type of template (character, environment, etc.)
            theme (str): Theme to apply
            style (str): Style preset to use
            customizations (Dict): Specific customizations
            
        Returns:
            Dict: Customized template data
        """
        # Get base components
        template = self.get_template(template_type)
        theme_config = self.get_theme(theme)
        style_config = self.get_style_preset(style)
        
        # Apply customizations
        customized_svg = self._apply_customizations(
            template['svg_base'], 
            theme_config, 
            style_config, 
            customizations
        )
        
        # Generate CSS animations if needed
        animations = self._generate_animations(
            template_type, 
            customizations.get('animation', 'idle'),
            theme_config
        )
        
        return {
            'svg_content': customized_svg,
            'css_animations': animations,
            'theme': theme,
            'style': style,
            'template_type': template_type,
            'customizations': customizations,
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'theme_colors': theme_config['colors'],
                'style_properties': style_config
            }
        }
    
    def generate_complete_html(self, customized_template: Dict, 
                              include_controls: bool = True) -> str:
        """Generate complete HTML file with the customized template"""
        
        theme_colors = customized_template['metadata']['theme_colors']
        
        html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mythiq Media - {customized_template['template_type'].title()}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, {theme_colors['background']}, {theme_colors['primary']});
            font-family: {customized_template['metadata']['theme_colors'].get('fonts', ['Arial', 'sans-serif'])[0]};
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            color: {theme_colors['text']};
        }}
        
        .media-container {{
            text-align: center;
            background: rgba(0,0,0,0.7);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            max-width: 90vw;
            max-height: 90vh;
            overflow: auto;
        }}
        
        .media-content {{
            margin: 20px 0;
        }}
        
        .media-svg {{
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }}
        
        .controls {{
            margin-top: 20px;
            display: flex;
            gap: 10px;
            justify-content: center;
            flex-wrap: wrap;
        }}
        
        .control-button {{
            background: linear-gradient(45deg, {theme_colors['secondary']}, {theme_colors['accent']});
            border: none;
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 14px;
            transition: transform 0.3s ease;
        }}
        
        .control-button:hover {{
            transform: scale(1.05);
        }}
        
        .info-panel {{
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            text-align: left;
            font-size: 12px;
        }}
        
        {customized_template['css_animations']}
    </style>
</head>
<body>
    <div class="media-container">
        <h2>🎨 {customized_template['template_type'].title()} - {customized_template['theme'].title()} Theme</h2>
        
        <div class="media-content">
            {customized_template['svg_content']}
        </div>
        
        {self._generate_controls_html(customized_template) if include_controls else ''}
        
        <div class="info-panel">
            <strong>Template Info:</strong><br>
            Type: {customized_template['template_type'].title()}<br>
            Theme: {customized_template['theme'].title()}<br>
            Style: {customized_template['style'].title()}<br>
            Generated: {customized_template['metadata']['generated_at'][:19]}
        </div>
    </div>
    
    <script>
        {self._generate_javascript_controls(customized_template)}
    </script>
</body>
</html>
        '''
        
        return html_content
    
    def _apply_customizations(self, svg_base: str, theme_config: Dict, 
                            style_config: Dict, customizations: Dict) -> str:
        """Apply theme, style, and custom modifications to SVG"""
        
        # Replace color placeholders
        svg_content = svg_base
        colors = theme_config['colors']
        
        svg_content = svg_content.replace('{{PRIMARY_COLOR}}', colors['primary'])
        svg_content = svg_content.replace('{{SECONDARY_COLOR}}', colors['secondary'])
        svg_content = svg_content.replace('{{ACCENT_COLOR}}', colors['accent'])
        svg_content = svg_content.replace('{{BACKGROUND_COLOR}}', colors['background'])
        svg_content = svg_content.replace('{{TEXT_COLOR}}', colors['text'])
        
        # Apply style modifications
        svg_content = svg_content.replace('{{STROKE_WIDTH}}', str(style_config['stroke_width']))
        svg_content = svg_content.replace('{{CORNER_RADIUS}}', str(style_config['corner_radius']))
        
        # Apply specific customizations
        for key, value in customizations.items():
            placeholder = f'{{{{{key.upper()}}}}}'
            svg_content = svg_content.replace(placeholder, str(value))
        
        return svg_content
    
    def _generate_animations(self, template_type: str, animation_type: str, 
                           theme_config: Dict) -> str:
        """Generate CSS animations for the template"""
        
        animations = {
            'idle': '''
                @keyframes idle {
                    0%, 100% { transform: translateY(0px); }
                    50% { transform: translateY(-5px); }
                }
                .animated-element { animation: idle 3s ease-in-out infinite; }
            ''',
            'pulse': '''
                @keyframes pulse {
                    0%, 100% { transform: scale(1); opacity: 1; }
                    50% { transform: scale(1.05); opacity: 0.8; }
                }
                .animated-element { animation: pulse 2s ease-in-out infinite; }
            ''',
            'glow': f'''
                @keyframes glow {{
                    0%, 100% {{ filter: drop-shadow(0 0 5px {theme_config['colors']['accent']}); }}
                    50% {{ filter: drop-shadow(0 0 20px {theme_config['colors']['accent']}); }}
                }}
                .animated-element {{ animation: glow 2s ease-in-out infinite; }}
            ''',
            'rotate': '''
                @keyframes rotate {
                    from { transform: rotate(0deg); }
                    to { transform: rotate(360deg); }
                }
                .animated-element { animation: rotate 10s linear infinite; }
            '''
        }
        
        return animations.get(animation_type, animations['idle'])
    
    def _generate_controls_html(self, customized_template: Dict) -> str:
        """Generate HTML controls for the template"""
        
        template_type = customized_template['template_type']
        template_config = self.get_template(template_type)
        
        controls_html = '<div class="controls">'
        
        # Animation controls
        for animation in template_config['animation_options']:
            controls_html += f'''
                <button class="control-button" onclick="changeAnimation('{animation}')">
                    {animation.title()}
                </button>
            '''
        
        # Theme controls
        for theme_name in self.themes.keys():
            controls_html += f'''
                <button class="control-button" onclick="changeTheme('{theme_name}')">
                    {theme_name.title()}
                </button>
            '''
        
        controls_html += '</div>'
        return controls_html
    
    def _generate_javascript_controls(self, customized_template: Dict) -> str:
        """Generate JavaScript for interactive controls"""
        
        return '''
            function changeAnimation(animationType) {
                const element = document.querySelector('.animated-element');
                if (element) {
                    element.style.animation = 'none';
                    setTimeout(() => {
                        element.style.animation = animationType + ' 2s ease-in-out infinite';
                    }, 10);
                }
            }
            
            function changeTheme(themeName) {
                // This would typically reload with new theme
                alert('Theme change to ' + themeName + ' - would reload with new theme in full implementation');
            }
            
            function downloadSVG() {
                const svg = document.querySelector('.media-svg');
                const svgData = new XMLSerializer().serializeToString(svg);
                const blob = new Blob([svgData], {type: 'image/svg+xml'});
                const url = URL.createObjectURL(blob);
                
                const link = document.createElement('a');
                link.href = url;
                link.download = 'mythiq-media.svg';
                link.click();
                
                URL.revokeObjectURL(url);
            }
        '''
    
    def _get_character_svg_template(self) -> str:
        """Get base SVG template for characters"""
        return '''
<svg class="media-svg animated-element" width="300" height="400" viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg">
    <!-- Character Head -->
    <circle cx="150" cy="100" r="50" fill="{{PRIMARY_COLOR}}" stroke="{{SECONDARY_COLOR}}" stroke-width="{{STROKE_WIDTH}}" />
    
    <!-- Character Eyes -->
    <circle cx="135" cy="90" r="8" fill="{{TEXT_COLOR}}" />
    <circle cx="165" cy="90" r="8" fill="{{TEXT_COLOR}}" />
    <circle cx="135" cy="90" r="4" fill="{{BACKGROUND_COLOR}}" />
    <circle cx="165" cy="90" r="4" fill="{{BACKGROUND_COLOR}}" />
    
    <!-- Character Body -->
    <rect x="125" y="150" width="50" height="80" rx="{{CORNER_RADIUS}}" fill="{{SECONDARY_COLOR}}" stroke="{{ACCENT_COLOR}}" stroke-width="{{STROKE_WIDTH}}" />
    
    <!-- Character Arms -->
    <rect x="95" y="160" width="25" height="60" rx="{{CORNER_RADIUS}}" fill="{{PRIMARY_COLOR}}" stroke="{{SECONDARY_COLOR}}" stroke-width="{{STROKE_WIDTH}}" />
    <rect x="180" y="160" width="25" height="60" rx="{{CORNER_RADIUS}}" fill="{{PRIMARY_COLOR}}" stroke="{{SECONDARY_COLOR}}" stroke-width="{{STROKE_WIDTH}}" />
    
    <!-- Character Legs -->
    <rect x="135" y="230" width="15" height="70" rx="{{CORNER_RADIUS}}" fill="{{PRIMARY_COLOR}}" stroke="{{SECONDARY_COLOR}}" stroke-width="{{STROKE_WIDTH}}" />
    <rect x="155" y="230" width="15" height="70" rx="{{CORNER_RADIUS}}" fill="{{PRIMARY_COLOR}}" stroke="{{SECONDARY_COLOR}}" stroke-width="{{STROKE_WIDTH}}" />
    
    <!-- Character Feet -->
    <ellipse cx="142" cy="310" rx="12" ry="8" fill="{{ACCENT_COLOR}}" stroke="{{SECONDARY_COLOR}}" stroke-width="{{STROKE_WIDTH}}" />
    <ellipse cx="162" cy="310" rx="12" ry="8" fill="{{ACCENT_COLOR}}" stroke="{{SECONDARY_COLOR}}" stroke-width="{{STROKE_WIDTH}}" />
    
    <!-- Accessories (customizable) -->
    <rect x="140" y="70" width="20" height="10" rx="5" fill="{{ACCENT_COLOR}}" opacity="0.8" />
</svg>
        '''
    
    def _get_environment_svg_template(self) -> str:
        """Get base SVG template for environments"""
        return '''
<svg class="media-svg animated-element" width="600" height="400" viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
    <!-- Sky/Background -->
    <rect width="600" height="400" fill="url(#skyGradient)" />
    
    <!-- Ground -->
    <rect x="0" y="300" width="600" height="100" fill="{{PRIMARY_COLOR}}" />
    
    <!-- Background Elements -->
    <circle cx="100" cy="150" r="30" fill="{{SECONDARY_COLOR}}" opacity="0.7" />
    <circle cx="500" cy="120" r="40" fill="{{SECONDARY_COLOR}}" opacity="0.5" />
    
    <!-- Foreground Elements -->
    <rect x="200" y="250" width="40" height="50" rx="{{CORNER_RADIUS}}" fill="{{ACCENT_COLOR}}" stroke="{{SECONDARY_COLOR}}" stroke-width="{{STROKE_WIDTH}}" />
    <rect x="350" y="230" width="60" height="70" rx="{{CORNER_RADIUS}}" fill="{{ACCENT_COLOR}}" stroke="{{SECONDARY_COLOR}}" stroke-width="{{STROKE_WIDTH}}" />
    
    <!-- Decorative Elements -->
    <polygon points="50,300 80,250 110,300" fill="{{SECONDARY_COLOR}}" opacity="0.8" />
    <polygon points="450,300 480,240 510,300" fill="{{SECONDARY_COLOR}}" opacity="0.8" />
    
    <!-- Gradients -->
    <defs>
        <linearGradient id="skyGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:{{BACKGROUND_COLOR}};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{{PRIMARY_COLOR}};stop-opacity:1" />
        </linearGradient>
    </defs>
</svg>
        '''
    
    def _get_ui_element_svg_template(self) -> str:
        """Get base SVG template for UI elements"""
        return '''
<svg class="media-svg animated-element" width="200" height="60" viewBox="0 0 200 60" xmlns="http://www.w3.org/2000/svg">
    <!-- Button Background -->
    <rect x="10" y="10" width="180" height="40" rx="{{CORNER_RADIUS}}" fill="{{PRIMARY_COLOR}}" stroke="{{SECONDARY_COLOR}}" stroke-width="{{STROKE_WIDTH}}" />
    
    <!-- Button Highlight -->
    <rect x="15" y="15" width="170" height="5" rx="{{CORNER_RADIUS}}" fill="{{ACCENT_COLOR}}" opacity="0.6" />
    
    <!-- Button Text Area -->
    <rect x="20" y="25" width="160" height="20" rx="2" fill="transparent" />
    
    <!-- Icon Area -->
    <circle cx="40" cy="30" r="8" fill="{{ACCENT_COLOR}}" opacity="0.8" />
    <circle cx="40" cy="30" r="4" fill="{{TEXT_COLOR}}" />
</svg>
        '''
    
    def _get_effect_svg_template(self) -> str:
        """Get base SVG template for effects"""
        return '''
<svg class="media-svg animated-element" width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <!-- Central Effect -->
    <circle cx="100" cy="100" r="20" fill="{{ACCENT_COLOR}}" opacity="0.8" />
    
    <!-- Particle Effects -->
    <circle cx="80" cy="80" r="5" fill="{{SECONDARY_COLOR}}" opacity="0.6" />
    <circle cx="120" cy="80" r="5" fill="{{SECONDARY_COLOR}}" opacity="0.6" />
    <circle cx="80" cy="120" r="5" fill="{{SECONDARY_COLOR}}" opacity="0.6" />
    <circle cx="120" cy="120" r="5" fill="{{SECONDARY_COLOR}}" opacity="0.6" />
    
    <!-- Glow Effect -->
    <circle cx="100" cy="100" r="40" fill="none" stroke="{{ACCENT_COLOR}}" stroke-width="2" opacity="0.3" />
    <circle cx="100" cy="100" r="60" fill="none" stroke="{{ACCENT_COLOR}}" stroke-width="1" opacity="0.2" />
    
    <!-- Burst Lines -->
    <line x1="100" y1="40" x2="100" y2="20" stroke="{{SECONDARY_COLOR}}" stroke-width="3" opacity="0.7" />
    <line x1="100" y1="160" x2="100" y2="180" stroke="{{SECONDARY_COLOR}}" stroke-width="3" opacity="0.7" />
    <line x1="40" y1="100" x2="20" y2="100" stroke="{{SECONDARY_COLOR}}" stroke-width="3" opacity="0.7" />
    <line x1="160" y1="100" x2="180" y2="100" stroke="{{SECONDARY_COLOR}}" stroke-width="3" opacity="0.7" />
</svg>
        '''

# Example usage and testing
if __name__ == "__main__":
    # Initialize the Template Manager
    manager = TemplateManager()
    
    print("🧪 Testing Template Manager:")
    print("=" * 40)
    
    # Test template customization
    customizations = {
        'animation': 'glow',
        'size': 'large',
        'special_effect': 'true'
    }
    
    result = manager.customize_template('character', 'ninja', 'cartoon', customizations)
    
    print(f"Template Type: {result['template_type']}")
    print(f"Theme: {result['theme']}")
    print(f"Style: {result['style']}")
    print(f"SVG Length: {len(result['svg_content'])} characters")
    print(f"CSS Length: {len(result['css_animations'])} characters")
    
    # Generate complete HTML
    html_output = manager.generate_complete_html(result)
    print(f"Complete HTML Length: {len(html_output)} characters")
    
    print("\n🎨 Template Manager ready for production use!")

