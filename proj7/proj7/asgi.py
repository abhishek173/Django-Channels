import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj7.settings')

from channels.routing import ProtocolTypeRouter, URLRouter

import app.routing 

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : URLRouter(
        app.routing.websocket_patterns
    )
})
