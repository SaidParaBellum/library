from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from my_music.views import MusicView, MusicUpdateView, MusicDetailView, MusicDeleteView, MusicCreateView

urlpatterns = [
    path('music_list', MusicView.as_view(), name='music_list'),
    path('create_music', MusicCreateView.as_view(), name='create_music'),
    path('update_music/<int:pk>', MusicUpdateView.as_view(), name='update_music'),
    path('detail_music/<int:pk>', MusicDetailView.as_view(), name='detail_music'),
    path('delete_music/<int:pk>', MusicDeleteView.as_view(), name='delete_music'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)