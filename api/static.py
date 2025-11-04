"""
Static files handler for Vercel
"""
import os
from pathlib import Path
from django.http import FileResponse, Http404
from django.conf import settings

def serve_static(request, path):
    """Serve static files in Vercel"""
    # Try to find the file in static directory
    static_dirs = settings.STATICFILES_DIRS if hasattr(settings, 'STATICFILES_DIRS') else []
    
    for static_dir in static_dirs:
        file_path = Path(static_dir) / path
        if file_path.exists() and file_path.is_file():
            response = FileResponse(open(file_path, 'rb'))
            # Set appropriate content type
            if path.endswith('.css'):
                response['Content-Type'] = 'text/css'
            elif path.endswith('.js'):
                response['Content-Type'] = 'application/javascript'
            elif path.endswith('.png'):
                response['Content-Type'] = 'image/png'
            elif path.endswith('.jpg') or path.endswith('.jpeg'):
                response['Content-Type'] = 'image/jpeg'
            elif path.endswith('.svg'):
                response['Content-Type'] = 'image/svg+xml'
            return response
    
    # Try staticfiles directory (collected static files)
    if hasattr(settings, 'STATIC_ROOT') and settings.STATIC_ROOT:
        file_path = Path(settings.STATIC_ROOT) / path
        if file_path.exists() and file_path.is_file():
            response = FileResponse(open(file_path, 'rb'))
            if path.endswith('.css'):
                response['Content-Type'] = 'text/css'
            elif path.endswith('.js'):
                response['Content-Type'] = 'application/javascript'
            return response
    
    raise Http404("Static file not found")

