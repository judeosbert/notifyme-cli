#!/usr/bin/env python3
"""
Example demonstrating the new notify-me usage patterns
"""

import subprocess
import sys
import time

def simulate_work(task_name, duration=2):
    """Simulate some work being done."""
    print(f"Starting {task_name}...")
    time.sleep(duration)
    print(f"{task_name} completed!")
    return True

def main():
    """Demonstrate different usage patterns."""
    
    print("=== notify-me Usage Examples ===\n")
    
    # Example 1: Simple notification after task
    print("1. Running task with default notification:")
    simulate_work("Data processing", 1)
    
    print("   Command: python task.py && notify-me")
    print("   (This would send 'Task complete' message)\n")
    
    # Example 2: Custom message
    print("2. Running task with custom notification:")
    simulate_work("Model training", 1)
    
    print("   Command: python train.py && notify-me -m 'Training finished!'")
    print("   (This would send 'Training finished!' message)\n")
    
    # Example 3: Complex pipeline
    print("3. Complex pipeline example:")
    simulate_work("Build", 0.5)
    simulate_work("Test", 0.5)
    simulate_work("Deploy", 0.5)
    
    print("   Command: make build && npm test && deploy.sh && notify-me -m 'Pipeline complete!'")
    print("   (This would send 'Pipeline complete!' message)\n")
    
    print("=== All examples completed! ===")
    print("Note: In real usage, each task would be followed by: && notify-me")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())