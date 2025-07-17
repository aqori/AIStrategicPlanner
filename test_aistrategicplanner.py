# test_aistrategicplanner.py
"""
Tests for AIStrategicPlanner module.
"""

import unittest
from aistrategicplanner import AIStrategicPlanner

class TestAIStrategicPlanner(unittest.TestCase):
    """Test cases for AIStrategicPlanner class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AIStrategicPlanner()
        self.assertIsInstance(instance, AIStrategicPlanner)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AIStrategicPlanner()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
