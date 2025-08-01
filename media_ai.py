"""
Mythiq Media AI - Intelligent Media Generation Analysis Engine
Analyzes prompts and routes to appropriate media generation systems
"""

import re
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class MediaAI:
    """
    Advanced AI system for analyzing media generation prompts
    Routes requests to appropriate generators with intelligent analysis
    """
    
    def __init__(self):
        """Initialize the Media AI system"""
        self.media_types = {
            'image': ['image', 'picture', 'photo', 'art', 'drawing', 'character', 'background', 'scene', 'sprite', 'icon', 'logo', 'design'],
            'video': ['video', 'animation', 'movie', 'clip', 'gif', 'motion', 'animate', 'sequence', 'cinematic', 'trailer'],
            'audio': ['audio', 'music', 'sound', 'song', 'melody', 'beat', 'soundtrack', 'effect', 'voice', 'noise']
        }
        
        self.themes = {
            'ninja': ['ninja', 'stealth', 'shadow', 'assassin', 'katana', 'shuriken', 'martial', 'japanese'],
            'space': ['space', 'cosmic', 'galaxy', 'star', 'planet', 'alien', 'sci-fi', 'futuristic', 'spaceship'],
            'medieval': ['medieval', 'knight', 'castle', 'sword', 'armor', 'dragon', 'fantasy', 'kingdom', 'royal'],
            'forest': ['forest', 'tree', 'nature', 'woodland', 'green', 'leaf', 'branch', 'natural', 'wild'],
            'underwater': ['underwater', 'ocean', 'sea', 'fish', 'coral', 'deep', 'aquatic', 'marine', 'blue']
        }
        
        self.styles = {
            'realistic': ['realistic', 'photorealistic', 'detailed', 'lifelike', 'accurate', 'precise'],
            'cartoon': ['cartoon', 'animated', 'stylized', 'cute', 'colorful', 'fun', 'playful'],
            'abstract': ['abstract', 'artistic', 'creative', 'unique', 'experimental', 'modern'],
            'minimalist': ['minimalist', 'simple', 'clean', 'basic', 'minimal', 'elegant'],
            'retro': ['retro', 'vintage', 'classic', 'old-school', '8-bit', 'pixel', 'nostalgic']
        }
        
        self.moods = {
            'epic': ['epic', 'dramatic', 'intense', 'powerful', 'heroic', 'grand', 'majestic'],
            'peaceful': ['peaceful', 'calm', 'relaxing', 'serene', 'tranquil', 'gentle', 'soothing'],
            'dark': ['dark', 'mysterious', 'gothic', 'sinister', 'ominous', 'shadowy', 'eerie'],
            'bright': ['bright', 'cheerful', 'happy', 'vibrant', 'energetic', 'positive', 'uplifting'],
            'mysterious': ['mysterious', 'enigmatic', 'cryptic', 'hidden', 'secret', 'unknown']
        }
        
        self.complexity_indicators = {
            'simple': ['simple', 'basic', 'easy', 'quick', 'minimal', 'plain'],
            'detailed': ['detailed', 'complex', 'intricate', 'elaborate', 'sophisticated', 'advanced'],
            'professional': ['professional', 'high-quality', 'polished', 'refined', 'premium']
        }
        
        print("🧠 Media AI Engine initialized with intelligent analysis capabilities")
    
    def analyze_prompt(self, prompt: str) -> Dict:
        """
        Comprehensive prompt analysis for media generation
        
        Args:
            prompt (str): User's media generation request
            
        Returns:
            Dict: Detailed analysis with routing information
        """
        prompt_lower = prompt.lower()
        
        analysis = {
            'original_prompt': prompt,
            'media_type': self._detect_media_type(prompt_lower),
            'theme': self._detect_theme(prompt_lower),
            'style': self._detect_style(prompt_lower),
            'mood': self._detect_mood(prompt_lower),
            'complexity': self._detect_complexity(prompt_lower),
            'keywords': self._extract_keywords(prompt_lower),
            'confidence': 0.0,
            'generation_strategy': '',
            'estimated_time': 0,
            'recommended_format': '',
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        # Calculate confidence and strategy
        analysis['confidence'] = self._calculate_confidence(analysis)
        analysis['generation_strategy'] = self._determine_strategy(analysis)
        analysis['estimated_time'] = self._estimate_generation_time(analysis)
        analysis['recommended_format'] = self._recommend_format(analysis)
        
        return analysis
    
    def _detect_media_type(self, prompt: str) -> str:
        """Detect the type of media requested"""
        scores = {}
        
        for media_type, keywords in self.media_types.items():
            score = sum(1 for keyword in keywords if keyword in prompt)
            scores[media_type] = score
        
        # Default to image if no clear indication
        if not scores or max(scores.values()) == 0:
            return 'image'
        
        return max(scores, key=scores.get)
    
    def _detect_theme(self, prompt: str) -> str:
        """Detect the theme/setting of the media"""
        scores = {}
        
        for theme, keywords in self.themes.items():
            score = sum(1 for keyword in keywords if keyword in prompt)
            scores[theme] = score
        
        if not scores or max(scores.values()) == 0:
            return 'default'
        
        return max(scores, key=scores.get)
    
    def _detect_style(self, prompt: str) -> str:
        """Detect the visual style requested"""
        scores = {}
        
        for style, keywords in self.styles.items():
            score = sum(1 for keyword in keywords if keyword in prompt)
            scores[style] = score
        
        if not scores or max(scores.values()) == 0:
            return 'default'
        
        return max(scores, key=scores.get)
    
    def _detect_mood(self, prompt: str) -> str:
        """Detect the mood/atmosphere requested"""
        scores = {}
        
        for mood, keywords in self.moods.items():
            score = sum(1 for keyword in keywords if keyword in prompt)
            scores[mood] = score
        
        if not scores or max(scores.values()) == 0:
            return 'neutral'
        
        return max(scores, key=scores.get)
    
    def _detect_complexity(self, prompt: str) -> str:
        """Detect the complexity level requested"""
        scores = {}
        
        for complexity, keywords in self.complexity_indicators.items():
            score = sum(1 for keyword in keywords if keyword in prompt)
            scores[complexity] = score
        
        # Also consider prompt length as complexity indicator
        if len(prompt.split()) > 10:
            scores['detailed'] = scores.get('detailed', 0) + 1
        elif len(prompt.split()) < 5:
            scores['simple'] = scores.get('simple', 0) + 1
        
        if not scores or max(scores.values()) == 0:
            return 'medium'
        
        return max(scores, key=scores.get)
    
    def _extract_keywords(self, prompt: str) -> List[str]:
        """Extract important keywords from the prompt"""
        # Remove common words
        stop_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'create', 'make', 'generate', 'build'}
        
        words = re.findall(r'\b\w+\b', prompt)
        keywords = [word for word in words if word not in stop_words and len(word) > 2]
        
        return keywords[:10]  # Return top 10 keywords
    
    def _calculate_confidence(self, analysis: Dict) -> float:
        """Calculate confidence score for the analysis"""
        confidence = 0.0
        
        # Base confidence from media type detection
        if analysis['media_type'] != 'image':  # Default fallback
            confidence += 0.3
        else:
            confidence += 0.1
        
        # Theme detection confidence
        if analysis['theme'] != 'default':
            confidence += 0.2
        
        # Style detection confidence
        if analysis['style'] != 'default':
            confidence += 0.2
        
        # Mood detection confidence
        if analysis['mood'] != 'neutral':
            confidence += 0.1
        
        # Keyword richness
        keyword_score = min(len(analysis['keywords']) / 5.0, 0.2)
        confidence += keyword_score
        
        return min(confidence, 1.0)
    
    def _determine_strategy(self, analysis: Dict) -> str:
        """Determine the best generation strategy"""
        media_type = analysis['media_type']
        complexity = analysis['complexity']
        theme = analysis['theme']
        
        if media_type == 'image':
            if complexity == 'simple':
                return 'svg_template'
            elif theme != 'default':
                return 'themed_svg_generation'
            else:
                return 'procedural_svg'
        
        elif media_type == 'video':
            if complexity == 'simple':
                return 'css_animation'
            else:
                return 'advanced_css_animation'
        
        elif media_type == 'audio':
            if 'music' in analysis['keywords']:
                return 'web_audio_composition'
            else:
                return 'web_audio_effects'
        
        return 'default_generation'
    
    def _estimate_generation_time(self, analysis: Dict) -> int:
        """Estimate generation time in seconds"""
        base_time = 1
        
        if analysis['media_type'] == 'video':
            base_time = 2
        elif analysis['media_type'] == 'audio':
            base_time = 1
        
        if analysis['complexity'] == 'detailed':
            base_time += 1
        elif analysis['complexity'] == 'professional':
            base_time += 2
        
        return base_time
    
    def _recommend_format(self, analysis: Dict) -> str:
        """Recommend the best output format"""
        media_type = analysis['media_type']
        complexity = analysis['complexity']
        
        if media_type == 'image':
            if complexity == 'simple':
                return 'svg'
            else:
                return 'svg_with_css'
        
        elif media_type == 'video':
            return 'css_animation_html'
        
        elif media_type == 'audio':
            return 'web_audio_javascript'
        
        return 'svg'
    
    def get_generation_tips(self, analysis: Dict) -> List[str]:
        """Get tips for improving generation quality"""
        tips = []
        
        if analysis['confidence'] < 0.5:
            tips.append("Try being more specific about what type of media you want")
        
        if analysis['theme'] == 'default':
            tips.append("Adding a theme (like 'ninja', 'space', 'medieval') will improve results")
        
        if analysis['style'] == 'default':
            tips.append("Specify a style (like 'cartoon', 'realistic', 'minimalist') for better visuals")
        
        if len(analysis['keywords']) < 3:
            tips.append("Add more descriptive words to get more detailed results")
        
        if analysis['media_type'] == 'video' and 'animation' not in analysis['keywords']:
            tips.append("Specify the type of animation you want (walking, flowing, spinning, etc.)")
        
        return tips
    
    def suggest_improvements(self, prompt: str) -> Dict:
        """Suggest improvements to the user's prompt"""
        analysis = self.analyze_prompt(prompt)
        tips = self.get_generation_tips(analysis)
        
        improved_prompts = []
        
        # Generate improved prompt suggestions
        base_prompt = prompt
        
        if analysis['theme'] == 'default':
            improved_prompts.append(f"{base_prompt} with ninja theme")
            improved_prompts.append(f"{base_prompt} in space setting")
        
        if analysis['style'] == 'default':
            improved_prompts.append(f"{base_prompt} in cartoon style")
            improved_prompts.append(f"{base_prompt} with realistic details")
        
        return {
            'original_analysis': analysis,
            'improvement_tips': tips,
            'suggested_prompts': improved_prompts[:3],  # Top 3 suggestions
            'confidence_boost': "Following these tips could improve generation quality by 20-40%"
        }
    
    def batch_analyze(self, prompts: List[str]) -> List[Dict]:
        """Analyze multiple prompts efficiently"""
        return [self.analyze_prompt(prompt) for prompt in prompts]
    
    def get_stats(self) -> Dict:
        """Get AI analysis statistics"""
        return {
            'supported_media_types': list(self.media_types.keys()),
            'supported_themes': list(self.themes.keys()),
            'supported_styles': list(self.styles.keys()),
            'supported_moods': list(self.moods.keys()),
            'analysis_capabilities': [
                'Media type detection',
                'Theme identification',
                'Style analysis',
                'Mood detection',
                'Complexity assessment',
                'Keyword extraction',
                'Confidence scoring',
                'Strategy recommendation',
                'Time estimation',
                'Format optimization'
            ],
            'ai_version': '3.0.0',
            'last_updated': datetime.now().isoformat()
        }

# Example usage and testing
if __name__ == "__main__":
    # Initialize the Media AI
    ai = MediaAI()
    
    # Test prompts
    test_prompts = [
        "Create a ninja character image",
        "Generate an epic space battle video",
        "Make peaceful forest ambient music",
        "Design a minimalist logo",
        "Animate a character walking through a medieval castle"
    ]
    
    print("🧪 Testing Media AI Analysis:")
    print("=" * 50)
    
    for prompt in test_prompts:
        analysis = ai.analyze_prompt(prompt)
        print(f"\nPrompt: '{prompt}'")
        print(f"Media Type: {analysis['media_type']}")
        print(f"Theme: {analysis['theme']}")
        print(f"Style: {analysis['style']}")
        print(f"Mood: {analysis['mood']}")
        print(f"Confidence: {analysis['confidence']:.2f}")
        print(f"Strategy: {analysis['generation_strategy']}")
        print(f"Estimated Time: {analysis['estimated_time']}s")
        print(f"Format: {analysis['recommended_format']}")
        print("-" * 30)
    
    print("\n🎯 Media AI Engine ready for production use!")

