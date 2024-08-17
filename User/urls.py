from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path

from User.views import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),

]  +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
