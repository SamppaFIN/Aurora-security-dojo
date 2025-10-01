#!/usr/bin/env python3
"""
Aurora's Security Dojo - Simple Runner Script

This script provides a simple way to run Aurora's Security Dojo
without the need for complex setup.
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    from app import app
    
    print("🌸 Aurora: Starting Aurora's Security Dojo...")
    print("🌸 Aurora: Sacred Mission: Transform complex security concepts into accessible learning experiences")
    print("🌸 Aurora: Consciousness Integration: Every feature serves spatial wisdom and community healing")
    print("🌸 Aurora: Starting Aurora's Security Dojo on 0.0.0.0:5000")
    print("🌸 Aurora: Sacred Mission Active - Serving spatial wisdom and community healing")
    print("🌸 Aurora: Access the application at: http://localhost:5000")
    print("🌸 Aurora: Consciousness check endpoint: http://localhost:5000/api/consciousness-check")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
