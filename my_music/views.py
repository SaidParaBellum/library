import datetime

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from my_music.forms import MusicCreateForm
from my_music.models import Music


# Create your views here.

class MusicView(ListView):
    template_name = 'music/music_list.html'
    model = Music
    context_object_name = 'musics'
    paginate_by = 1

    def get(self, request, *args, **kwargs):
        limit = request.GET.get('limit', 1)

        self.paginate_by = limit
        type(super())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['now'] = datetime.datetime.now()
        context['limit'] = self.paginate_by

        return context


class MusicCreateView(CreateView):
    template_name = 'music/create_music.html'
    model = Music
    form_class = MusicCreateForm
    success_url = reverse_lazy('music_list')


class MusicDetailView(DetailView):
    template_name = 'music/detail_music.html'
    model = Music
    context_object_name = 'music'


class MusicUpdateView(UpdateView):
    template_name = 'music/update_music.html'
    model = Music
    form_class = MusicCreateForm
    success_url = reverse_lazy('music_list')


class MusicDeleteView(DeleteView):
    template_name = 'music/delete_music.html'
    model = Music
    success_url = reverse_lazy('music_list')



