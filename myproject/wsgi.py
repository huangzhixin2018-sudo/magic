"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Add project root to Python path for Vercel
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

# Vercel requires 'app' variable
app = application

# Handle static files in development
if os.environ.get('DJANGO_SETTINGS_MODULE') == 'myproject.settings':
    from django.conf import settings
    from django.contrib.staticfiles.handlers import StaticFilesHandler
    if settings.DEBUG:
        application = StaticFilesHandler(application)
