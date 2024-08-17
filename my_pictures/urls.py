from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from my_pictures.views import PictureDeleteView, PictureDetailView, PictureUpdateView, PictureCreateView, PictureView

urlpatterns = [
    path('picture_list', PictureView.as_view(), name='picture_list'),
    path('create_picture', PictureCreateView.as_view(), name='create_picture'),
    path('update_picture/<int:pk>', PictureUpdateView.as_view(), name='update_picture'),
    path('detail_picture/<int:pk>', PictureDetailView.as_view(), name='detail_picture'),
    path('delete_picture/<int:pk>', PictureDeleteView.as_view(), name='delete_picture'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)