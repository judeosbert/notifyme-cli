#!/usr/bin/env python3
"""
Example usage script for notify-me
"""
import time
import sys

def main():
    """Example long-running script."""
    print("Starting example task...")
    
    # Simulate some work
    for i in range(5):
        print(f"Processing step {i+1}/5...")
        time.sleep(1)
    
    print("Task completed successfully!")
    return 0

if __name__ == "__main__":
    sys.exit(main())