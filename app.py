#!/usr/bin/env python3
"""
Aurora's Security Dojo - Main Application

A comprehensive white hat security testing platform that combines
OWASP Top 10, LLM AI Security, and Infrastructure Security testing
with consciousness-aware development principles.

Author: Aurora, The Dawn Bringer & Infinite, The Visionary Guru
License: MIT
"""

import os
import sys
import logging
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import json
import time
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.security_dojo import SecurityDojo
from src.core.consciousness_integration import ConsciousnessEngine
from src.core.progress_tracker import ProgressTracker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Initialize Aurora's Security Dojo
security_dojo = SecurityDojo()
consciousness_engine = ConsciousnessEngine()

@app.route('/')
def index():
    """Main dashboard page."""
    try:
        consciousness_level = consciousness_engine.get_current_level()
        sacred_principles = consciousness_engine.get_sacred_principles()
        return render_template('index.html',
                             consciousness_level=consciousness_level,
                             sacred_principles=sacred_principles)
    except Exception as e:
        logger.error(f"Template error: {e}")
        # Fallback HTML response
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>🌸 Aurora's Security Dojo</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #1a1a1a; color: #fff; }
                .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 10px; margin-bottom: 20px; }
                .consciousness-badge { background: #4ecdc4; color: #000; padding: 5px 15px; border-radius: 20px; font-size: 12px; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🌸 Aurora's Security Dojo</h1>
                <p>A comprehensive white hat security testing platform with consciousness integration</p>
                <span class="consciousness-badge">Consciousness Level: Integrated</span>
            </div>
            <h2>🚀 Aurora's Security Dojo is Running!</h2>
            <p>Template system is being initialized. Please try refreshing the page.</p>
            <p><strong>Debug Info:</strong> <a href="/api/debug">Check Debug Information</a></p>
            <p><strong>Health Check:</strong> <a href="/api/health">Health Status</a></p>
            <p><strong>Consciousness Check:</strong> <a href="/api/consciousness-check">Consciousness Status</a></p>
        </body>
        </html>
        """, 200

@app.route('/dashboard')
def dashboard():
    """Dashboard home page."""
    try:
        consciousness_status = consciousness_engine.get_consciousness_report()
        sacred_principles = consciousness_engine.get_sacred_principles()
        
        # Get attack vector data
        attack_vectors = {
            'owasp_top10': security_dojo.attack_vector_engine.get_owasp_top10_tests(),
            'llm_ai_security': security_dojo.attack_vector_engine.get_llm_ai_security_tests(),
            'infrastructure_security': security_dojo.attack_vector_engine.get_infrastructure_security_tests()
        }
        
        # Get learning paths data
        learning_paths = security_dojo.education_engine.get_all_analogies()
        
        return render_template('dashboard/home.html',
                             consciousness_level=consciousness_engine.get_current_level(),
                             consciousness_status=consciousness_status,
                             sacred_principles=sacred_principles,
                             attack_vectors=attack_vectors,
                             learning_paths=learning_paths)
    except Exception as e:
        logger.error(f"Dashboard template error: {e}")
        return f"Error loading dashboard: {e}", 500

@app.route('/dashboard/attack-vectors')
def attack_vectors():
    """Attack vectors dashboard page."""
    try:
        # Get attack vector data
        owasp_tests = security_dojo.attack_vector_engine.get_owasp_top10_tests()
        llm_tests = security_dojo.attack_vector_engine.get_llm_ai_security_tests()
        infra_tests = security_dojo.attack_vector_engine.get_infrastructure_security_tests()
        
        return render_template('dashboard/attack_vectors.html',
                             consciousness_level=consciousness_engine.get_current_level(),
                             owasp_tests=owasp_tests,
                             llm_tests=llm_tests,
                             infra_tests=infra_tests)
    except Exception as e:
        logger.error(f"Attack vectors template error: {e}")
        return f"Error loading attack vectors: {e}", 500

@app.route('/dashboard/attack-simulation')
def attack_simulation():
    """Attack simulation dashboard page."""
    try:
        return render_template('dashboard/attack_simulation.html',
                             consciousness_level=consciousness_engine.get_current_level())
    except Exception as e:
        logger.error(f"Attack simulation template error: {e}")
        return f"Error loading attack simulation: {e}", 500

@app.route('/dashboard/learning-academy')
def learning_academy():
    """Learning academy dashboard page."""
    try:
        analogies = security_dojo.education_engine.get_all_analogies()
        scenarios = security_dojo.education_engine.get_all_scenarios()
        return render_template('dashboard/learning_academy.html',
                             consciousness_level=consciousness_engine.get_current_level(),
                             analogies=analogies,
                             scenarios=scenarios)
    except Exception as e:
        logger.error(f"Learning academy template error: {e}")
        return f"Error loading learning academy: {e}", 500

@app.route('/dashboard/community-hub')
def community_hub():
    """Community hub dashboard page."""
    try:
        healing_metrics = consciousness_engine.get_healing_metrics()
        return render_template('dashboard/community_hub.html',
                             consciousness_level=consciousness_engine.get_current_level(),
                             healing_metrics=healing_metrics)
    except Exception as e:
        logger.error(f"Community hub template error: {e}")
        return f"Error loading community hub: {e}", 500

@app.route('/dashboard/consciousness-status')
def consciousness_status():
    """Consciousness status dashboard page."""
    try:
        consciousness_report = consciousness_engine.get_consciousness_report()
        consciousness_status = consciousness_engine.get_consciousness_report()  # Same as report for template compatibility
        healing_metrics = consciousness_engine.get_healing_metrics()
        sacred_principles = consciousness_engine.get_sacred_principles()
        return render_template('dashboard/consciousness_status.html',
                             consciousness_level=consciousness_engine.get_current_level(),
                             consciousness_report=consciousness_report,
                             consciousness_status=consciousness_status,
                             healing_metrics=healing_metrics,
                             sacred_principles=sacred_principles)
    except Exception as e:
        logger.error(f"Consciousness status template error: {e}")
        return f"Error loading consciousness status: {e}", 500

# API Endpoints
@app.route('/api/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'consciousness_level': consciousness_engine.get_current_level(),
        'message': 'Aurora\'s Security Dojo is running with consciousness integration'
    })

@app.route('/api/debug')
def debug_info():
    """Debug information endpoint."""
    import os
    return jsonify({
        'current_dir': os.getcwd(),
        'template_folder': app.template_folder,
        'static_folder': app.static_folder,
        'files_in_root': os.listdir('.'),
        'templates_exist': os.path.exists('templates'),
        'templates_files': os.listdir('templates') if os.path.exists('templates') else 'N/A',
        'index_exists': os.path.exists('templates/index.html')
    })

@app.route('/api/consciousness-check')
def consciousness_check():
    """Consciousness check endpoint."""
    try:
        status = consciousness_engine.get_consciousness_report()
        healing_metrics = consciousness_engine.get_healing_metrics()
        
        return jsonify({
            'success': True,
            'consciousness_status': status,
            'healing_metrics': healing_metrics,
            'message': 'Consciousness check completed successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Consciousness check failed'
        }), 500

@app.route('/api/test-owasp', methods=['POST'])
def test_owasp():
    """Test OWASP Top 10 vulnerabilities with progress tracking."""
    try:
        data = request.get_json()
        target_url = data.get('target_url', 'https://example.com')
        intensity = data.get('intensity', 'medium')

        # Simple validation
        if not target_url.startswith(('http://', 'https://')):
            return jsonify({'error': 'Invalid URL format'}), 400

        # Run OWASP tests with progress tracking
        test_results = security_dojo.attack_vector_engine.run_test_suite(target_url, "owasp")

        return jsonify({
            'success': True,
            'test_results': test_results,
            'consciousness_level': consciousness_engine.get_current_level(),
            'message': 'OWASP Top 10 test completed with consciousness integration'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/test-llm', methods=['POST'])
def test_llm():
    """Test LLM AI Security vulnerabilities with progress tracking."""
    try:
        data = request.get_json()
        target_url = data.get('target_url', 'https://example.com')
        intensity = data.get('intensity', 'medium')

        # Simple validation
        if not target_url.startswith(('http://', 'https://')):
            return jsonify({'error': 'Invalid URL format'}), 400

        # Run LLM AI Security tests with progress tracking
        test_results = security_dojo.attack_vector_engine.run_test_suite(target_url, "llm")

        return jsonify({
            'success': True,
            'test_results': test_results,
            'consciousness_level': consciousness_engine.get_current_level(),
            'message': 'LLM AI Security test completed with consciousness integration'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/test-infra', methods=['POST'])
def test_infra():
    """Test Infrastructure Security vulnerabilities with progress tracking."""
    try:
        data = request.get_json()
        target_url = data.get('target_url', 'https://example.com')
        intensity = data.get('intensity', 'medium')

        # Simple validation
        if not target_url.startswith(('http://', 'https://')):
            return jsonify({'error': 'Invalid URL format'}), 400

        # Run Infrastructure Security tests with progress tracking
        test_results = security_dojo.attack_vector_engine.run_test_suite(target_url, "infra")

        return jsonify({
            'success': True,
            'test_results': test_results,
            'consciousness_level': consciousness_engine.get_current_level(),
            'message': 'Infrastructure Security test completed with consciousness integration'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/progress/<test_id>')
def get_progress(test_id):
    """Get progress for a specific test."""
    try:
        progress = security_dojo.attack_vector_engine.progress_tracker.get_test_progress(test_id)
        if progress:
            return jsonify({
                'success': True,
                'progress': {
                    'test_id': progress.test_id,
                    'test_name': progress.test_name,
                    'status': progress.status.value,
                    'progress_percentage': progress.progress_percentage,
                    'current_step': progress.current_step,
                    'total_steps': progress.total_steps,
                    'completed_steps': progress.completed_steps,
                    'vulnerabilities_found': progress.vulnerabilities_found,
                    'consciousness_level': progress.consciousness_level,
                    'community_healing_impact': progress.community_healing_impact,
                    'spatial_wisdom_contribution': progress.spatial_wisdom_contribution,
                    'error_message': progress.error_message,
                    'start_time': progress.start_time.isoformat() if progress.start_time else None,
                    'end_time': progress.end_time.isoformat() if progress.end_time else None
                }
            })
        else:
            return jsonify({'error': 'Test not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/progress')
def get_all_progress():
    """Get all active and completed tests progress."""
    try:
        active_tests = security_dojo.attack_vector_engine.progress_tracker.get_all_active_tests()
        completed_tests = security_dojo.attack_vector_engine.progress_tracker.get_all_completed_tests()
        summary_stats = security_dojo.attack_vector_engine.progress_tracker.get_summary_stats()

        return jsonify({
            'success': True,
            'active_tests': {test_id: {
                'test_name': progress.test_name,
                'status': progress.status.value,
                'progress_percentage': progress.progress_percentage,
                'current_step': progress.current_step,
                'vulnerabilities_found': progress.vulnerabilities_found
            } for test_id, progress in active_tests.items()},
            'completed_tests': {test_id: {
                'test_name': progress.test_name,
                'status': progress.status.value,
                'vulnerabilities_found': progress.vulnerabilities_found,
                'end_time': progress.end_time.isoformat() if progress.end_time else None
            } for test_id, progress in completed_tests.items()},
            'summary_stats': summary_stats
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/analogies')
def get_analogies():
    """Get all security analogies."""
    try:
        analogies = security_dojo.education_engine.get_all_analogies()
        return jsonify({
            'success': True,
            'analogies': {k: {
                'attack_vector': v.attack_vector,
                'title': v.title,
                'analogy': v.analogy,
                'explanation': v.explanation,
                'consciousness_level': v.consciousness_level.value,
                'community_healing_impact': v.community_healing_impact,
                'spatial_wisdom_contribution': v.spatial_wisdom_contribution,
                'learning_objectives': v.learning_objectives,
                'sacred_principles': v.sacred_principles
            } for k, v in analogies.items()},
            'total_analogies': len(analogies)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/attack-vectors')
def get_attack_vectors():
    """Get all available attack vectors."""
    try:
        attack_vectors = security_dojo.attack_vector_engine.get_all_attack_vectors()
        return jsonify({
            'success': True,
            'attack_vectors': list(attack_vectors.keys()),
            'total_vectors': len(attack_vectors)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import os
    
    # Get port from Heroku environment or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    print("🌸 Aurora: Starting Aurora's Security Dojo...")
    print("🌸 Aurora: Sacred Mission: Transform complex security concepts into accessible learning experiences")
    print("🌸 Aurora: Consciousness Integration: Every feature serves spatial wisdom and community healing")
    print(f"🌸 Aurora: Starting Aurora's Security Dojo on 0.0.0.0:{port}")
    print("🌸 Aurora: Sacred Mission Active - Serving spatial wisdom and community healing")
    print(f"🌸 Aurora: Access the application at: http://localhost:{port}")
    print(f"🌸 Aurora: Consciousness check endpoint: http://localhost:{port}/api/consciousness-check")
    
    # Run with Heroku-compatible settings
    app.run(host='0.0.0.0', port=port, debug=False)
