# 🎨 Mythiq Media Creator

**Advanced AI-Powered Media Generation Service**

Generate professional-quality images, videos, and audio using intelligent AI analysis and procedural generation techniques. Built for Railway deployment with zero external dependencies.

## 🌟 Features

### 🖼️ **Image Generation**
- **5 Character Types**: Humanoid, warrior, mage, creature, robot
- **5 Environment Themes**: Space, forest, medieval, underwater, abstract
- **Professional SVG Output**: Scalable, animated, theme-aware
- **No External APIs**: 100% free, unlimited usage

### 🎬 **Video Generation**
- **CSS Animation System**: Smooth, professional animations
- **Multiple Animation Types**: Character movement, environment effects, UI transitions
- **Customizable Duration**: 5-60 seconds
- **HTML5 Compatible**: Works in all modern browsers

### 🎵 **Audio Generation**
- **Web Audio API**: High-quality synthesis
- **5 Music Styles**: Epic, peaceful, dark, bright, mysterious
- **Sound Effects**: Game sounds, UI sounds, ambient audio
- **Interactive Controls**: Volume, tempo, style adjustments

### 🎨 **Template Management**
- **Advanced Theming**: 5 complete visual themes
- **Style Presets**: Cartoon, realistic, minimalist, fantasy
- **Dynamic Customization**: Real-time theme and style changes
- **Asset Management**: Organized template system

## 🚀 Quick Start

### Railway Deployment

1. **Create Repository**
   ```bash
   git clone <your-repo-url>
   cd mythiq-media-creator
   ```

2. **Deploy to Railway**
   - Connect your GitHub repository
   - Railway auto-detects Python app
   - Deploys in 2-3 minutes

3. **Test the Service**
   ```bash
   curl https://your-service.up.railway.app/health
   ```

### Local Development

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Service**
   ```bash
   python app.py
   ```

3. **Access the API**
   - Service runs on `http://localhost:5003`
   - Health check: `http://localhost:5003/health`

## 📡 API Endpoints

### **Image Generation**
```bash
POST /api/generate/image
Content-Type: application/json

{
  "prompt": "Create a ninja character for my game",
  "theme": "ninja",
  "style": "cartoon",
  "animation": "idle"
}
```

**Response:**
```json
{
  "success": true,
  "format": "svg_html",
  "content": "<html>...</html>",
  "generation_time": 1.2,
  "theme": "ninja",
  "style": "cartoon"
}
```

### **Video Generation**
```bash
POST /api/generate/video
Content-Type: application/json

{
  "prompt": "Character walking animation",
  "duration": 30,
  "animation_type": "character_movement"
}
```

### **Audio Generation**
```bash
POST /api/generate/audio
Content-Type: application/json

{
  "prompt": "Epic battle music",
  "style": "epic",
  "duration": 45
}
```

### **Health Check**
```bash
GET /health
```

**Response:**
```json
{
  "service": "mythiq-media-creator",
  "status": "healthy",
  "health_score": 95,
  "capabilities": {
    "image_generation": "operational",
    "video_generation": "operational",
    "audio_generation": "operational"
  }
}
```

## 🧠 AI Analysis Engine

The Media AI analyzes prompts using advanced pattern recognition:

### **Prompt Analysis**
- **Media Type Detection**: Automatically determines if user wants image, video, or audio
- **Theme Recognition**: Identifies themes like ninja, space, medieval, etc.
- **Style Analysis**: Detects preferred visual style (cartoon, realistic, etc.)
- **Complexity Assessment**: Determines generation complexity level
- **Confidence Scoring**: Provides confidence in analysis accuracy

### **Example Analysis**
```
Input: "Create a ninja character for my stealth game"

Analysis:
- Media Type: image (95% confidence)
- Theme: ninja (92% confidence)
- Style: cartoon (78% confidence)
- Complexity: medium
- Keywords: [character, ninja, stealth, game]
```

## 🎨 Themes & Styles

### **Available Themes**
1. **Ninja** - Dark, stealthy, mysterious
2. **Space** - Futuristic, cosmic, technological
3. **Medieval** - Ancient, heroic, ornate
4. **Forest** - Natural, peaceful, organic
5. **Underwater** - Flowing, calm, aquatic

### **Style Presets**
1. **Cartoon** - Bold, colorful, friendly
2. **Realistic** - Detailed, natural, sophisticated
3. **Minimalist** - Clean, simple, modern
4. **Fantasy** - Magical, elaborate, imaginative

## 🔧 Technical Architecture

### **Core Components**
- **Media AI** (`media_ai.py`) - Intelligent prompt analysis
- **Image Generator** (`image_generator.py`) - SVG-based image creation
- **Video Generator** (`video_generator.py`) - CSS animation system
- **Audio Generator** (`audio_generator.py`) - Web Audio API synthesis
- **Template Manager** (`template_manager.py`) - Asset management
- **Health Checker** (`health_check.py`) - Service monitoring

### **Technology Stack**
- **Backend**: Python 3.11, Flask
- **Image Generation**: SVG, CSS3
- **Video Generation**: CSS Animations, HTML5
- **Audio Generation**: Web Audio API, JavaScript
- **Deployment**: Railway, Docker-compatible

### **Performance Specs**
- **Image Generation**: 0.8-2.0 seconds
- **Video Generation**: 1.5-3.0 seconds
- **Audio Generation**: 1.0-2.5 seconds
- **Memory Usage**: 80-150MB
- **CPU Usage**: Low (optimized algorithms)

## 🌐 Integration

### **With Mythiq Assistant**
```python
# mythiq-assistant routes media requests here
response = requests.post(
    'https://mythiq-media-creator.up.railway.app/api/generate/image',
    json={'prompt': user_message}
)
```

### **With Mythiq UI**
```javascript
// Frontend integration
const generateMedia = async (prompt, type) => {
  const response = await fetch(`/api/generate/${type}`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({prompt})
  });
  return response.json();
};
```

## 📊 Monitoring & Health

### **Health Metrics**
- **System Metrics**: CPU, memory, disk usage
- **Service Metrics**: Request count, success rate, generation times
- **Capability Status**: All generation systems operational
- **Performance History**: Detailed performance tracking

### **Error Handling**
- **Graceful Degradation**: Service continues with reduced functionality
- **Detailed Logging**: Comprehensive error tracking
- **Automatic Recovery**: Self-healing capabilities
- **Fallback Responses**: Always provides useful output

## 🔒 Security & Privacy

### **Data Privacy**
- **No Data Storage**: Prompts and generated content not stored
- **No External APIs**: All processing happens locally
- **No User Tracking**: Privacy-focused design
- **Secure Processing**: Input validation and sanitization

### **Rate Limiting**
- **Built-in Protection**: Prevents abuse
- **Configurable Limits**: Adjustable per deployment
- **Fair Usage**: Ensures service availability

## 🚀 Deployment Options

### **Railway (Recommended)**
- **One-click deployment**
- **Auto-scaling**
- **Built-in monitoring**
- **Custom domains**

### **Docker**
```dockerfile
FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### **Local Development**
```bash
python app.py
# Service available at http://localhost:5003
```

## 📈 Performance Optimization

### **Generation Speed**
- **Template-based**: Pre-built components for fast assembly
- **Procedural Generation**: Algorithmic content creation
- **Caching**: Intelligent template caching
- **Parallel Processing**: Multi-threaded where possible

### **Memory Efficiency**
- **Lightweight Dependencies**: Minimal external libraries
- **Efficient Algorithms**: Optimized generation code
- **Garbage Collection**: Proper memory management
- **Resource Monitoring**: Real-time usage tracking

## 🤝 Contributing

### **Development Setup**
1. Fork the repository
2. Create feature branch
3. Install dependencies: `pip install -r requirements.txt`
4. Run tests: `python -m pytest`
5. Submit pull request

### **Adding New Themes**
1. Add theme configuration to `template_manager.py`
2. Create theme-specific templates
3. Update documentation
4. Test with all media types

### **Adding New Media Types**
1. Create generator class
2. Add to `media_ai.py` analysis
3. Update API endpoints
4. Add health checks

## 📝 License

MIT License - see LICENSE file for details.

## 🆘 Support

### **Documentation**
- **API Reference**: `/docs` endpoint
- **Health Dashboard**: `/health` endpoint
- **Performance Metrics**: `/metrics` endpoint

### **Troubleshooting**
- **Check Health**: `GET /health`
- **View Logs**: Railway dashboard
- **Test Capabilities**: `GET /test`

### **Contact**
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Email**: support@mythiq.ai

---

**Built with ❤️ for the Mythiq AI Creative Platform**

*Empowering creators with intelligent, free, and unlimited media generation.*

