#!/usr/bin/env python3
"""Fix requirements.txt encoding from UTF-16 to UTF-8 with proper deps."""

import os
from pathlib import Path

req_file = Path(__file__).parent / 'requirements.txt'

# Read with UTF-16 handling
try:
    content = req_file.read_bytes()
    if content[:2] == b'\xff\xfe':
        text = content.decode('utf-16-le')
    else:
        text = content.decode('utf-8', errors='ignore')
except Exception as e:
    print(f"Error reading: {e}")
    exit(1)

# Keep only essential deps
deps = [
    'Flask==3.1.3',
    'requests==2.31.0', 
    'python-dotenv==1.0.0',
    'Werkzeug==3.1.8'
]

# Write back as UTF-8
req_file.write_text('\n'.join(deps) + '\n', encoding='utf-8')
print("✓ requirements.txt fixed to UTF-8 with essential dependencies")
