from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
    )
    ))
    
})