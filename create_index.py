#!/usr/bin/env python3
"""
Create index.html - Quick script to regenerate frontend
Run from project root: python create_index.py
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.create_index import create_index_html

if __name__ == "__main__":
    create_index_html()

