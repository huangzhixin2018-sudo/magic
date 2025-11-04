"""
Vercel serverless function entry point for Django
"""
import os
import sys
from pathlib import Path

# Add the project root to the Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Import Django and get WSGI application
from django.core.wsgi import get_wsgi_application

# This is what Vercel will use as the WSGI application
application = get_wsgi_application()

