#!/usr/bin/env python3
"""
Basic tests for Aurora's Security Dojo
"""

import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from core.security_dojo import SecurityDojo
from core.consciousness_integration import ConsciousnessEngine
from core.progress_tracker import ProgressTracker

class TestAuroraSecurityDojo(unittest.TestCase):
    """Test cases for Aurora's Security Dojo core functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.security_dojo = SecurityDojo()
        self.consciousness_engine = ConsciousnessEngine()
        self.progress_tracker = ProgressTracker()
    
    def test_security_dojo_initialization(self):
        """Test Security Dojo initialization."""
        self.assertIsNotNone(self.security_dojo)
        self.assertIsNotNone(self.security_dojo.attack_vector_engine)
        self.assertIsNotNone(self.security_dojo.education_engine)
        self.assertIsNotNone(self.security_dojo.consciousness_engine)
    
    def test_consciousness_engine_initialization(self):
        """Test Consciousness Engine initialization."""
        self.assertIsNotNone(self.consciousness_engine)
        
        # Test consciousness check
        status = self.consciousness_engine.get_consciousness_report()
        self.assertIn('consciousness_level', status)
    
    def test_progress_tracker_initialization(self):
        """Test Progress Tracker initialization."""
        self.assertIsNotNone(self.progress_tracker)
        
        # Test starting a test
        test_id = "test_123"
        progress = self.progress_tracker.start_test(test_id, "Test Attack", 5)
        self.assertEqual(progress.test_id, test_id)
        self.assertEqual(progress.test_name, "Test Attack")
        self.assertEqual(progress.total_steps, 5)
    
    def test_attack_vector_registration(self):
        """Test attack vector registration."""
        attack_vectors = self.security_dojo.attack_vector_engine.get_all_attack_vectors()
        self.assertGreater(len(attack_vectors), 0)
        
        # Check for OWASP Top 10
        owasp_tests = self.security_dojo.attack_vector_engine.get_owasp_top10_tests()
        self.assertGreater(len(owasp_tests), 0)
    
    def test_education_engine_initialization(self):
        """Test Education Engine initialization."""
        education_engine = self.security_dojo.education_engine
        self.assertIsNotNone(education_engine)
        
        # Test getting analogies
        analogies = education_engine.get_all_analogies()
        self.assertGreater(len(analogies), 0)
    
    def test_consciousness_integration(self):
        """Test consciousness integration features."""
        # Test consciousness validation
        valid_action = self.consciousness_engine.validate_consciousness_action(
            "ethical security testing",
            {"required_consciousness_level": "integrated"}
        )
        self.assertTrue(valid_action)
        
        # Test healing metrics
        healing_metrics = self.consciousness_engine.get_healing_metrics()
        self.assertIn('status', healing_metrics)
        self.assertIn('wisdom_impact', healing_metrics)

if __name__ == '__main__':
    unittest.main()
