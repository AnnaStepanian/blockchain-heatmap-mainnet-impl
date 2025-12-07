#!/usr/bin/env python3
"""
Simple HTTP server to serve frontend files with CORS support
This allows the HTML to fetch JSON data without CORS errors
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
FRONTEND_DIR = PROJECT_ROOT / "frontend"
PORT = 8000


class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with CORS support"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(FRONTEND_DIR), **kwargs)
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()


def main():
    """Start the HTTP server"""
    os.chdir(FRONTEND_DIR)
    
    try:
        with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
            url = f"http://localhost:{PORT}/index.html"
            print("=" * 60)
            print("Bitcoin Node Map Server")
            print("=" * 60)
            print(f"Server running at: {url}")
            print(f"Serving files from: {FRONTEND_DIR}")
            print("\nThe map will automatically update every 10 seconds")
            print("Press Ctrl+C to stop the server")
            print("=" * 60)
            
            webbrowser.open(url)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"Error: Port {PORT} is already in use.")
            print(f"Please close the application using port {PORT} or change the PORT in serve.py")
        else:
            print(f"Error starting server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

