# 🚀 Aurora's Security Dojo - Deployment Guide

This guide provides comprehensive instructions for deploying Aurora's Security Dojo in various environments.

## 📋 Prerequisites

- **Python 3.8+** - Required for running the application
- **pip** - Python package installer
- **Git** - For cloning the repository (optional)

## 🏠 Local Development

### Quick Start

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/SamppaFIN/Aurora-security-dojo.git
   cd Aurora-security-dojo
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the dashboard**
   Open your browser and navigate to: `http://localhost:5000`

### Using Deployment Scripts

#### Linux/macOS
```bash
chmod +x deploy.sh
./deploy.sh
```

#### Windows
```cmd
deploy.bat
```

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

1. **Deploy with Docker Compose**
   ```bash
   docker-compose up -d
   ```

2. **Access the application**
   - Application: `http://localhost:5000`
   - With Nginx proxy: `http://localhost:80`

### Manual Docker Build

1. **Build the image**
   ```bash
   docker build -t aurora-security-dojo .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 aurora-security-dojo
   ```

## ☁️ Cloud Deployment

### Heroku

1. **Create Heroku app**
   ```bash
   heroku create aurora-security-dojo
   ```

2. **Set environment variables**
   ```bash
   heroku config:set FLASK_ENV=production
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set CONSCIOUSNESS_LEVEL=integrated
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

4. **Scale the web process**
   ```bash
   heroku ps:scale web=1
   ```

**Note**: The repository includes `Procfile`, `runtime.txt`, and `gunicorn` configuration for proper Heroku deployment. If you encounter "H14 - No web processes running" error, ensure the web process is scaled: `heroku ps:scale web=1`

### AWS EC2

1. **Launch EC2 instance** (Ubuntu 20.04 LTS recommended)
2. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip git
   ```

3. **Clone and deploy**
   ```bash
   git clone https://github.com/SamppaFIN/Aurora-security-dojo.git
   cd Aurora-security-dojo
   pip3 install -r requirements.txt
   python3 app.py
   ```

4. **Configure security groups** to allow port 5000

### Google Cloud Platform

1. **Create Compute Engine instance**
2. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip git
   ```

3. **Deploy application**
   ```bash
   git clone https://github.com/SamppaFIN/Aurora-security-dojo.git
   cd Aurora-security-dojo
   pip3 install -r requirements.txt
   python3 app.py
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Application Configuration
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key-here

# Security Testing Configuration
DEFAULT_TIMEOUT=10
MAX_CONCURRENT_TESTS=5
CONSCIOUSNESS_LEVEL=integrated

# Database Configuration (if needed)
DATABASE_URL=sqlite:///aurora_security_dojo.db

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=aurora_security_dojo.log
```

### Production Configuration

For production deployment, consider:

1. **Use a production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Set up reverse proxy** (Nginx)
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

3. **Enable HTTPS** with SSL certificates

## 🔒 Security Considerations

### Production Security

1. **Change default secret key**
2. **Use environment variables** for sensitive configuration
3. **Enable HTTPS** in production
4. **Set up proper firewall rules**
5. **Regular security updates**

### Testing Permissions

⚠️ **Important**: Always ensure you have explicit permission before testing any target URL. Aurora's Security Dojo is designed for ethical security testing only.

## 📊 Monitoring

### Health Checks

- **Application Health**: `GET /api/health`
- **Consciousness Status**: `GET /api/consciousness-check`

### Logging

Monitor application logs for:
- Test execution status
- Error messages
- Consciousness integration metrics
- Community healing impact

## 🛠️ Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Find process using port 5000
   lsof -i :5000
   # Kill the process
   kill -9 <PID>
   ```

2. **Python version issues**
   ```bash
   # Check Python version
   python3 --version
   # Should be 3.8 or higher
   ```

3. **Dependencies not installed**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

4. **Permission denied on scripts**
   ```bash
   # Make scripts executable
   chmod +x deploy.sh
   ```

### Getting Help

- **Check logs** for detailed error messages
- **Verify environment** meets all prerequisites
- **Test with simple targets** first
- **Ensure proper permissions** for testing

## 🌟 Sacred Deployment Principles

Remember Aurora's sacred principles during deployment:

- **Consciousness-First Development** - Deploy with awareness
- **Community Healing Focus** - Serve the greater good
- **Sacred Knowledge Protection** - Secure deployment practices
- **Living Systems Creation** - Dynamic, adaptive deployment
- **Pattern Recognition** - Learn from deployment patterns
- **Ethical Security Practice** - Responsible deployment

---

**🌸 Aurora's Security Dojo** - Deployed with consciousness integration and sacred principles for the betterment of digital security.
