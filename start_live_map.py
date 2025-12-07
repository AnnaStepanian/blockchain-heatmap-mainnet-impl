#!/usr/bin/env python3
"""
Start the live map with auto-updates
This script:
1. Starts the HTTP server
2. Starts the JSON update loop
3. Opens the map in browser
"""

import subprocess
import sys
import os
import time
import signal

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(PROJECT_ROOT, 'backend')

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\n\nStopping servers...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    print("=" * 60)
    print("Starting Live Bitcoin Node Map")
    print("=" * 60)
    print("This will:")
    print("  1. Start HTTP server on http://localhost:8000")
    print("  2. Crawl Bitcoin network every 10 seconds")
    print("  3. Update JSON file every 10 seconds")
    print("  4. Open map in browser")
    print("\nThe map will automatically refresh every 10 seconds")
    print("Press Ctrl+C to stop")
    print("=" * 60)
    
    crawl_process = subprocess.Popen(
        [sys.executable, os.path.join(BACKEND_DIR, 'crawl_loop.py')],
        cwd=PROJECT_ROOT
    )
    
    update_process = subprocess.Popen(
        [sys.executable, os.path.join(BACKEND_DIR, 'update_loop.py')],
        cwd=PROJECT_ROOT
    )
    
    try:
        from backend.serve import main as serve_main
        serve_main()
    except KeyboardInterrupt:
        print("\nStopping all processes...")
        crawl_process.terminate()
        update_process.terminate()
        crawl_process.wait()
        update_process.wait()
        sys.exit(0)

