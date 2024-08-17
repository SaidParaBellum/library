import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from my_video.forms import VideoCreateForm
from my_video.models import Video


# Create your views here.

class VideoView(ListView):
    template_name = 'video/video_list.html'
    model = Video
    context_object_name = 'videos'
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

class VideoCreateView(CreateView):
    template_name = 'video/create_video.html'
    model = Video
    form_class = VideoCreateForm
    success_url = reverse_lazy('video_list')

class VideoDetailView(DetailView):
    template_name = 'video/detail_video.html'
    model = Video
    context_object_name = 'video'

class VideoUpdateView(UpdateView):
    template_name = 'video/update_video.html'
    model = Video
    form_class = VideoCreateForm
    success_url = reverse_lazy('video_list')

class VideoDeleteView(DeleteView):
    template_name = 'video/delete_video.html'
    model = Video
    success_url = reverse_lazy('video_list')


