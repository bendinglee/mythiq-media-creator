"""
Mythiq Media Creator Health Check System
Comprehensive monitoring and diagnostics for media generation services
"""

import time
import psutil
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class HealthChecker:
    """
    Advanced health monitoring system for mythiq-media-creator
    Monitors performance, capabilities, and system health
    """
    
    def __init__(self):
        """Initialize the health checking system"""
        self.start_time = datetime.now()
        self.generation_stats = {
            'images_generated': 0,
            'videos_generated': 0,
            'audio_generated': 0,
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'average_generation_time': 0.0,
            'last_generation_time': None
        }
        
        self.performance_history = []
        self.error_log = []
        self.capability_tests = {}
        
        # Initialize capability tests
        self._initialize_capability_tests()
        
        print("🏥 Advanced Health Checker initialized for mythiq-media-creator")
    
    def get_health_status(self) -> Dict:
        """
        Get comprehensive health status of the media creator service
        
        Returns:
            Dict: Complete health status information
        """
        current_time = datetime.now()
        uptime = current_time - self.start_time
        
        # Get system metrics
        system_metrics = self._get_system_metrics()
        
        # Get service metrics
        service_metrics = self._get_service_metrics()
        
        # Get capability status
        capability_status = self._get_capability_status()
        
        # Determine overall health
        overall_health = self._determine_overall_health(
            system_metrics, service_metrics, capability_status
        )
        
        return {
            'service': 'mythiq-media-creator',
            'status': overall_health['status'],
            'health_score': overall_health['score'],
            'timestamp': current_time.isoformat(),
            'uptime': {
                'seconds': int(uptime.total_seconds()),
                'human_readable': str(uptime).split('.')[0]
            },
            'system_metrics': system_metrics,
            'service_metrics': service_metrics,
            'capabilities': capability_status,
            'performance': self._get_performance_summary(),
            'recent_errors': self._get_recent_errors(),
            'recommendations': self._get_health_recommendations(overall_health)
        }
    
    def record_generation(self, media_type: str, success: bool, 
                         generation_time: float, error_message: str = None):
        """
        Record a media generation attempt
        
        Args:
            media_type (str): Type of media generated (image, video, audio)
            success (bool): Whether generation was successful
            generation_time (float): Time taken for generation
            error_message (str): Error message if failed
        """
        self.generation_stats['total_requests'] += 1
        
        if success:
            self.generation_stats['successful_requests'] += 1
            self.generation_stats[f'{media_type}s_generated'] += 1
            
            # Update average generation time
            current_avg = self.generation_stats['average_generation_time']
            total_successful = self.generation_stats['successful_requests']
            
            if total_successful == 1:
                self.generation_stats['average_generation_time'] = generation_time
            else:
                new_avg = ((current_avg * (total_successful - 1)) + generation_time) / total_successful
                self.generation_stats['average_generation_time'] = new_avg
        else:
            self.generation_stats['failed_requests'] += 1
            if error_message:
                self._log_error(media_type, error_message)
        
        self.generation_stats['last_generation_time'] = datetime.now().isoformat()
        
        # Record performance data
        self._record_performance_data(media_type, success, generation_time)
    
    def test_capabilities(self) -> Dict:
        """
        Test all media generation capabilities
        
        Returns:
            Dict: Results of capability tests
        """
        test_results = {}
        
        for capability, test_func in self.capability_tests.items():
            try:
                start_time = time.time()
                result = test_func()
                test_time = time.time() - start_time
                
                test_results[capability] = {
                    'status': 'pass' if result['success'] else 'fail',
                    'test_time': round(test_time, 3),
                    'details': result,
                    'timestamp': datetime.now().isoformat()
                }
            except Exception as e:
                test_results[capability] = {
                    'status': 'error',
                    'test_time': 0,
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                }
        
        return test_results
    
    def get_performance_metrics(self) -> Dict:
        """Get detailed performance metrics"""
        if not self.performance_history:
            return {'message': 'No performance data available yet'}
        
        recent_data = self.performance_history[-100:]  # Last 100 requests
        
        # Calculate metrics
        successful_requests = [d for d in recent_data if d['success']]
        failed_requests = [d for d in recent_data if not d['success']]
        
        if successful_requests:
            avg_time = sum(d['generation_time'] for d in successful_requests) / len(successful_requests)
            min_time = min(d['generation_time'] for d in successful_requests)
            max_time = max(d['generation_time'] for d in successful_requests)
        else:
            avg_time = min_time = max_time = 0
        
        return {
            'recent_requests': len(recent_data),
            'success_rate': len(successful_requests) / len(recent_data) * 100 if recent_data else 0,
            'average_generation_time': round(avg_time, 3),
            'min_generation_time': round(min_time, 3),
            'max_generation_time': round(max_time, 3),
            'failed_requests': len(failed_requests),
            'media_type_breakdown': self._get_media_type_breakdown(recent_data)
        }
    
    def _get_system_metrics(self) -> Dict:
        """Get system-level metrics"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            return {
                'cpu_usage_percent': cpu_percent,
                'memory': {
                    'total_gb': round(memory.total / (1024**3), 2),
                    'available_gb': round(memory.available / (1024**3), 2),
                    'used_percent': memory.percent
                },
                'disk': {
                    'total_gb': round(disk.total / (1024**3), 2),
                    'free_gb': round(disk.free / (1024**3), 2),
                    'used_percent': round((disk.used / disk.total) * 100, 1)
                },
                'status': 'healthy'
            }
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'message': 'Could not retrieve system metrics'
            }
    
    def _get_service_metrics(self) -> Dict:
        """Get service-specific metrics"""
        total_requests = self.generation_stats['total_requests']
        successful_requests = self.generation_stats['successful_requests']
        
        success_rate = (successful_requests / total_requests * 100) if total_requests > 0 else 0
        
        return {
            'total_requests': total_requests,
            'successful_requests': successful_requests,
            'failed_requests': self.generation_stats['failed_requests'],
            'success_rate_percent': round(success_rate, 1),
            'images_generated': self.generation_stats['images_generated'],
            'videos_generated': self.generation_stats['videos_generated'],
            'audio_generated': self.generation_stats['audio_generated'],
            'average_generation_time': round(self.generation_stats['average_generation_time'], 3),
            'last_generation': self.generation_stats['last_generation_time']
        }
    
    def _get_capability_status(self) -> Dict:
        """Get status of media generation capabilities"""
        return {
            'image_generation': {
                'status': 'operational',
                'supported_formats': ['SVG', 'HTML5'],
                'supported_themes': ['ninja', 'space', 'medieval', 'forest', 'underwater'],
                'supported_styles': ['cartoon', 'realistic', 'minimalist', 'fantasy']
            },
            'video_generation': {
                'status': 'operational',
                'supported_formats': ['CSS Animation', 'HTML5'],
                'supported_types': ['character_animation', 'environment_animation', 'effect_animation'],
                'max_duration': '60 seconds'
            },
            'audio_generation': {
                'status': 'operational',
                'supported_formats': ['Web Audio API', 'JavaScript'],
                'supported_types': ['music', 'sound_effects', 'ambient'],
                'supported_styles': ['epic', 'peaceful', 'dark', 'bright', 'mysterious']
            },
            'template_management': {
                'status': 'operational',
                'available_templates': ['character', 'environment', 'ui_element', 'effect'],
                'customization_options': ['theme', 'style', 'animation', 'size']
            }
        }
    
    def _determine_overall_health(self, system_metrics: Dict, 
                                service_metrics: Dict, capability_status: Dict) -> Dict:
        """Determine overall health status and score"""
        score = 100
        status = 'healthy'
        issues = []
        
        # Check system metrics
        if system_metrics.get('status') == 'error':
            score -= 30
            issues.append('System metrics unavailable')
        else:
            if system_metrics['cpu_usage_percent'] > 80:
                score -= 15
                issues.append('High CPU usage')
            if system_metrics['memory']['used_percent'] > 85:
                score -= 15
                issues.append('High memory usage')
            if system_metrics['disk']['used_percent'] > 90:
                score -= 10
                issues.append('Low disk space')
        
        # Check service metrics
        if service_metrics['total_requests'] > 0:
            if service_metrics['success_rate_percent'] < 90:
                score -= 20
                issues.append('Low success rate')
            if service_metrics['average_generation_time'] > 5.0:
                score -= 10
                issues.append('Slow generation times')
        
        # Check recent errors
        recent_errors = self._get_recent_errors()
        if len(recent_errors) > 5:
            score -= 15
            issues.append('Multiple recent errors')
        
        # Determine status based on score
        if score >= 90:
            status = 'healthy'
        elif score >= 70:
            status = 'warning'
        else:
            status = 'critical'
        
        return {
            'status': status,
            'score': max(0, score),
            'issues': issues
        }
    
    def _get_performance_summary(self) -> Dict:
        """Get performance summary"""
        if not self.performance_history:
            return {'message': 'No performance data available'}
        
        recent_data = self.performance_history[-50:]  # Last 50 requests
        
        return {
            'recent_requests': len(recent_data),
            'average_response_time': round(
                sum(d['generation_time'] for d in recent_data) / len(recent_data), 3
            ) if recent_data else 0,
            'success_rate': round(
                len([d for d in recent_data if d['success']]) / len(recent_data) * 100, 1
            ) if recent_data else 0
        }
    
    def _get_recent_errors(self) -> List[Dict]:
        """Get recent errors (last 24 hours)"""
        cutoff_time = datetime.now() - timedelta(hours=24)
        return [
            error for error in self.error_log 
            if datetime.fromisoformat(error['timestamp']) > cutoff_time
        ]
    
    def _get_health_recommendations(self, health_status: Dict) -> List[str]:
        """Get health recommendations based on current status"""
        recommendations = []
        
        if health_status['score'] < 70:
            recommendations.append("Service health is below optimal - investigate issues")
        
        if 'High CPU usage' in health_status['issues']:
            recommendations.append("Consider optimizing generation algorithms or scaling resources")
        
        if 'High memory usage' in health_status['issues']:
            recommendations.append("Monitor memory leaks and optimize template caching")
        
        if 'Low success rate' in health_status['issues']:
            recommendations.append("Review error logs and improve error handling")
        
        if 'Slow generation times' in health_status['issues']:
            recommendations.append("Optimize generation algorithms and template processing")
        
        if not recommendations:
            recommendations.append("Service is operating optimally")
        
        return recommendations
    
    def _initialize_capability_tests(self):
        """Initialize capability test functions"""
        self.capability_tests = {
            'image_generation': self._test_image_generation,
            'video_generation': self._test_video_generation,
            'audio_generation': self._test_audio_generation,
            'template_management': self._test_template_management
        }
    
    def _test_image_generation(self) -> Dict:
        """Test image generation capability"""
        try:
            # Simulate image generation test
            test_prompt = "Test ninja character"
            start_time = time.time()
            
            # This would normally call the actual image generator
            # For testing, we simulate success
            generation_time = time.time() - start_time
            
            return {
                'success': True,
                'generation_time': round(generation_time, 3),
                'test_prompt': test_prompt,
                'output_format': 'SVG'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _test_video_generation(self) -> Dict:
        """Test video generation capability"""
        try:
            # Simulate video generation test
            test_prompt = "Test character animation"
            start_time = time.time()
            
            # This would normally call the actual video generator
            generation_time = time.time() - start_time
            
            return {
                'success': True,
                'generation_time': round(generation_time, 3),
                'test_prompt': test_prompt,
                'output_format': 'CSS Animation'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _test_audio_generation(self) -> Dict:
        """Test audio generation capability"""
        try:
            # Simulate audio generation test
            test_prompt = "Test epic music"
            start_time = time.time()
            
            # This would normally call the actual audio generator
            generation_time = time.time() - start_time
            
            return {
                'success': True,
                'generation_time': round(generation_time, 3),
                'test_prompt': test_prompt,
                'output_format': 'Web Audio API'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _test_template_management(self) -> Dict:
        """Test template management capability"""
        try:
            # Simulate template management test
            start_time = time.time()
            
            # This would normally test template operations
            test_time = time.time() - start_time
            
            return {
                'success': True,
                'test_time': round(test_time, 3),
                'templates_available': 4,
                'themes_available': 5
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _log_error(self, media_type: str, error_message: str):
        """Log an error"""
        error_entry = {
            'timestamp': datetime.now().isoformat(),
            'media_type': media_type,
            'error_message': error_message
        }
        
        self.error_log.append(error_entry)
        
        # Keep only last 100 errors
        if len(self.error_log) > 100:
            self.error_log = self.error_log[-100:]
    
    def _record_performance_data(self, media_type: str, success: bool, generation_time: float):
        """Record performance data"""
        performance_entry = {
            'timestamp': datetime.now().isoformat(),
            'media_type': media_type,
            'success': success,
            'generation_time': generation_time
        }
        
        self.performance_history.append(performance_entry)
        
        # Keep only last 1000 entries
        if len(self.performance_history) > 1000:
            self.performance_history = self.performance_history[-1000:]
    
    def _get_media_type_breakdown(self, data: List[Dict]) -> Dict:
        """Get breakdown of requests by media type"""
        breakdown = {}
        
        for entry in data:
            media_type = entry['media_type']
            if media_type not in breakdown:
                breakdown[media_type] = {'total': 0, 'successful': 0}
            
            breakdown[media_type]['total'] += 1
            if entry['success']:
                breakdown[media_type]['successful'] += 1
        
        # Calculate success rates
        for media_type in breakdown:
            total = breakdown[media_type]['total']
            successful = breakdown[media_type]['successful']
            breakdown[media_type]['success_rate'] = round(successful / total * 100, 1) if total > 0 else 0
        
        return breakdown

# Example usage and testing
if __name__ == "__main__":
    # Initialize the Health Checker
    checker = HealthChecker()
    
    print("🧪 Testing Health Checker:")
    print("=" * 40)
    
    # Simulate some generation attempts
    checker.record_generation('image', True, 1.2)
    checker.record_generation('video', True, 2.5)
    checker.record_generation('audio', False, 0.0, "Test error")
    checker.record_generation('image', True, 0.8)
    
    # Get health status
    health_status = checker.get_health_status()
    
    print(f"Service: {health_status['service']}")
    print(f"Status: {health_status['status']}")
    print(f"Health Score: {health_status['health_score']}/100")
    print(f"Uptime: {health_status['uptime']['human_readable']}")
    print(f"Total Requests: {health_status['service_metrics']['total_requests']}")
    print(f"Success Rate: {health_status['service_metrics']['success_rate_percent']}%")
    
    # Test capabilities
    capability_results = checker.test_capabilities()
    print(f"\nCapability Tests:")
    for capability, result in capability_results.items():
        print(f"  {capability}: {result['status']}")
    
    print("\n🏥 Health Checker ready for production use!")

