from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from my_video.views import VideoView, VideoCreateView, VideoUpdateView, VideoDetailView, VideoDeleteView

urlpatterns = [
    path('video_list', VideoView.as_view(), name='video_list'),
    path('create_video', VideoCreateView.as_view(), name='create_video'),
    path('update_video/<int:pk>', VideoUpdateView.as_view(), name='update_video'),
    path('detail_video/<int:pk>', VideoDetailView.as_view(), name='detail_video'),
    path('delete_video/<int:pk>', VideoDeleteView.as_view(), name='delete_video'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)