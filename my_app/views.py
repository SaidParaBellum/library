
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from my_books.models import Book, FavoriteBook
from my_music.models import Music, FavoriteMusic
from my_video.models import Video, FavoriteVideo
from my_pictures.models import Picture, FavoritePicture


# Create your views here.

class IndexView(TemplateView):
    template_name = 'my_app/index.html'



@login_required
def profile(request):
    favorite_books = FavoriteBook.objects.filter(user=request.user).select_related('book')
    favorite_music = FavoriteMusic.objects.filter(user=request.user).select_related('music')
    favorite_videos = FavoriteVideo.objects.filter(user=request.user).select_related('video')
    favorite_pictures = FavoritePicture.objects.filter(user=request.user).select_related('picture')

    context = {
        'favorite_books': favorite_books,
        'favorite_music': favorite_music,
        'favorite_videos': favorite_videos,
        'favorite_pictures': favorite_pictures,
    }

    return render(request, 'auth/profile.html', context)

@login_required
def add_book_to_favorites(request, item_id):
    book = get_object_or_404(Book, id=item_id)
    FavoriteBook.objects.get_or_create(user=request.user, book=book)
    return redirect('profile')

@login_required
def add_music_to_favorites(request, item_id):
    music = get_object_or_404(Music, id=item_id)
    FavoriteMusic.objects.get_or_create(user=request.user, music=music)
    return redirect('profile')

@login_required
def add_video_to_favorites(request, item_id):
    video = get_object_or_404(Video, id=item_id)
    FavoriteVideo.objects.get_or_create(user=request.user, video=video)
    return redirect('profile')

@login_required
def add_picture_to_favorites(request, item_id):
    picture = get_object_or_404(Picture, id=item_id)
    FavoritePicture.objects.get_or_create(user=request.user, picture=picture)
    return redirect('profile')
