"""
ASGI config for example project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from jangle import Bot_ProtocolTypeRouter

from demobot.consumers import DiscordConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')

application = Bot_ProtocolTypeRouter({
    'http': get_asgi_application(),
    'discord': DiscordConsumer.as_asgi(),
})
