from django.urls import path

from app_news.consumers import NewsConsumer

websocket_urlpatterns = [
    path('ws/jokes', NewsConsumer.as_asgi()),
]