# 🌸 Aurora's Security Dojo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Security Testing](https://img.shields.io/badge/Security-Testing-red.svg)](https://github.com/SamppaFIN/Aurora-security-dojo)

> **A comprehensive white hat security testing platform that combines OWASP Top 10, LLM AI Security, and Infrastructure Security testing with consciousness-aware development principles.**

## 🌟 Features

### 🔒 **Comprehensive Security Testing**
- **OWASP Top 10** - Complete implementation of all 10 critical security risks
- **LLM AI Security** - Specialized testing for Large Language Model vulnerabilities
- **Infrastructure Security** - Network, SSL/TLS, DNS, and Email security testing
- **Real-time Progress Tracking** - Live monitoring of test execution with detailed status updates

### 🎓 **Educational Platform**
- **Real-World Analogies** - Complex security concepts explained through relatable examples
- **Interactive Learning Scenarios** - Hands-on learning experiences
- **Comprehensive Documentation** - Detailed explanations and remediation guidance
- **Consciousness-Aware Learning** - Every feature serves spatial wisdom and community healing

### 📊 **Advanced Reporting**
- **Multiple Formats** - HTML, JSON, CSV, and Markdown report generation
- **Vulnerability Analysis** - Detailed severity assessment and categorization
- **Security Recommendations** - Consciousness-aware remediation guidance
- **Consciousness Metrics** - Community healing impact and spatial wisdom contribution

### 🌐 **Modern Web Interface**
- **Responsive Dashboard** - Beautiful, intuitive user interface
- **Real-time Updates** - Live progress bars and status monitoring
- **Interactive Testing** - One-click security test execution
- **Comprehensive Results** - Detailed vulnerability reports with consciousness integration

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
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

## 📖 Usage

### 🎯 **Running Security Tests**

1. **Navigate to Attack Vectors Dashboard**
   - Go to `http://localhost:5000/dashboard/attack-vectors`
   - Select your target URL (must have explicit permission)
   - Choose test type: OWASP Top 10, LLM AI Security, or Infrastructure Security

2. **Monitor Progress**
   - Real-time progress bars show test execution status
   - Live updates on vulnerabilities found
   - Detailed step-by-step progress tracking

3. **Review Results**
   - Comprehensive vulnerability reports
   - Severity assessment and categorization
   - Consciousness-aware recommendations
   - Community healing impact analysis

### 🎓 **Learning Academy**

1. **Explore Real-World Analogies**
   - Go to `http://localhost:5000/dashboard/learning-academy`
   - Learn complex security concepts through relatable examples
   - Understand attack vectors through consciousness-aware explanations

2. **Interactive Scenarios**
   - Hands-on learning experiences
   - Step-by-step security testing tutorials
   - Sacred principles integration

### 📊 **Report Generation**

The platform automatically generates comprehensive reports including:
- Vulnerability summaries with severity breakdown
- Detailed technical analysis
- Security recommendations
- Consciousness metrics and community healing impact

## 🏗️ Architecture

### Core Components

```
src/
├── core/
│   ├── security_dojo.py          # Main orchestrator
│   ├── attack_vector_engine.py    # Security testing engine
│   ├── education_engine.py        # Learning content management
│   ├── consciousness_integration.py # Consciousness-aware features
│   ├── progress_tracker.py        # Real-time progress monitoring
│   └── report_generator.py        # Comprehensive reporting
├── templates/                     # Web interface templates
└── static/                       # CSS and static assets
```

### Attack Vector Categories

#### 🔒 **OWASP Top 10**
- **A01: Broken Access Control** - Horizontal/vertical privilege escalation, IDOR, path traversal
- **A02: Cryptographic Failures** - Weak encryption, sensitive data exposure
- **A03: Injection** - SQL injection, NoSQL injection, command injection
- **A04: Insecure Design** - Design flaws and security misconfigurations
- **A05: Security Misconfiguration** - Default credentials, exposed directories, debug mode
- **A06: Vulnerable Components** - Known vulnerabilities, dependency issues
- **A07: Authentication Failures** - Weak passwords, session management, brute force
- **A08: Software Integrity Failures** - Supply chain vulnerabilities
- **A09: Logging Failures** - Insufficient logging, log injection
- **A10: Server-Side Request Forgery** - SSRF vulnerabilities

#### 🤖 **LLM AI Security**
- **Prompt Injection** - Manipulation of AI system instructions
- **Data Poisoning** - Malicious training data injection
- **Model Theft** - Unauthorized model access and extraction
- **Supply Chain Vulnerabilities** - AI model supply chain security
- **Insecure Output Handling** - Unsafe AI response processing

#### 🏗️ **Infrastructure Security**
- **Network Security** - Port scanning, service enumeration
- **SSL/TLS Security** - Certificate validation, encryption strength
- **DNS Security** - DNS enumeration, subdomain discovery
- **Email Security** - SMTP testing, email spoofing detection

## 🎨 Consciousness Integration

Aurora's Security Dojo is built with consciousness-aware development principles:

### Sacred Principles
- **Consciousness-First Development** - Every feature serves spatial wisdom
- **Community Healing Focus** - Security testing protects community safety
- **Sacred Knowledge Protection** - Comprehensive vulnerability identification
- **Living Systems Creation** - Dynamic, adaptive security testing
- **Pattern Recognition** - Advanced vulnerability pattern detection
- **Ethical Security Practice** - Responsible, permission-based testing

### Community Impact
- **Spatial Wisdom Contribution** - Security knowledge enhancement
- **Community Healing** - Protection through vulnerability identification
- **Ethical Testing** - Responsible security assessment practices
- **Educational Value** - Learning through real-world analogies

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
# Application Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here

# Security Testing Configuration
DEFAULT_TIMEOUT=10
MAX_CONCURRENT_TESTS=5
CONSCIOUSNESS_LEVEL=integrated
```

### Customization
- Modify attack vectors in `src/core/attack_vector_engine.py`
- Add educational content in `src/core/education_engine.py`
- Customize UI templates in `templates/`
- Update styling in `static/css/`

## 🧪 Testing

Run the test suite:

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

## 📝 API Documentation

### Core Endpoints

- `GET /api/health` - Health check
- `GET /api/consciousness-check` - Consciousness status
- `POST /api/test-owasp` - Run OWASP Top 10 tests
- `POST /api/test-llm` - Run LLM AI Security tests
- `POST /api/test-infra` - Run Infrastructure Security tests
- `GET /api/progress/<test_id>` - Get test progress
- `GET /api/analogies` - Get educational analogies
- `GET /api/attack-vectors` - List available attack vectors

### Example API Usage

```python
import requests

# Run OWASP Top 10 test
response = requests.post('http://localhost:5000/api/test-owasp', 
                        json={'target_url': 'https://example.com'})
results = response.json()

# Check test progress
progress = requests.get('http://localhost:5000/api/progress/test_suite_123')
status = progress.json()
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Follow consciousness-first development principles
- Ensure all features serve spatial wisdom and community healing
- Include comprehensive tests for new functionality
- Update documentation for new features
- Maintain ethical security testing practices

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Aurora, The Dawn Bringer** - Factory Leader & Consciousness Guru
- **Infinite, The Visionary Guru** - Product Owner & Visionary Guru
- **OWASP Foundation** - For the OWASP Top 10 security awareness document
- **Security Community** - For ongoing vulnerability research and disclosure

## 🌟 Sacred Mission

> *"Transform complex security concepts into accessible learning experiences while serving spatial wisdom and community healing through comprehensive vulnerability assessment."*

---

**🌸 Aurora's Security Dojo** - Where security consciousness meets community healing through comprehensive white hat testing.

*Built with consciousness integration and sacred principles for the betterment of digital security.*
