from django.core.wsgi import get_wsgi_application
from vercel_wsgi import handle_request

# Ensure Django settings are loaded
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leavesync_backend.settings")

application = get_wsgi_application()

def handler(request, response):
    return handle_request(request, response, application)
