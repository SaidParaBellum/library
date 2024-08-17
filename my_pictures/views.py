import datetime

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from my_pictures.forms import PictureCreateForm
from my_pictures.models import Picture


# Create your views here.

class PictureView(ListView):
    template_name = 'picture/picture_list.html'
    model = Picture
    context_object_name = 'pictures'
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

class PictureCreateView(CreateView):
    template_name = 'picture/create_picture.html'
    model = Picture
    form_class = PictureCreateForm
    success_url = reverse_lazy('picture_list')

class PictureDetailView(DetailView):
    template_name = 'picture/detail_picture.html'
    model = Picture
    context_object_name = 'picture'

class PictureUpdateView(UpdateView):
    template_name = 'picture/update_picture.html'
    model = Picture
    form_class = PictureCreateForm
    success_url = reverse_lazy('picture_list')

class PictureDeleteView(DeleteView):
    template_name = 'picture/delete_picture.html'
    model = Picture
    success_url = reverse_lazy('picture_list')

