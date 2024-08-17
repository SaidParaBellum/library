from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from my_app.views import IndexView, add_book_to_favorites, add_music_to_favorites, add_video_to_favorites, \
    add_picture_to_favorites, profile
from my_books.views import BookCreateView, BookUpdateView, BookDetailView, BookDeleteView, BookView

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('list', BookView.as_view(), name='list'),
    path('create', BookCreateView.as_view(), name='create'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete'),
    path('book/add_to_favorites/<int:item_id>/', add_book_to_favorites, name='add_book_to_favorites'),
    path('music/add_to_favorites/<int:item_id>/', add_music_to_favorites, name='add_music_to_favorites'),
    path('video/add_to_favorites/<int:item_id>/', add_video_to_favorites, name='add_video_to_favorites'),
    path('picture/add_to_favorites/<int:item_id>/', add_picture_to_favorites, name='add_picture_to_favorites'),
    path('profile/', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)