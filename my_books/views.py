import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from my_books.forms import BookCreateForm
from my_books.models import Book


# Create your views here.


class BookView(ListView):
    template_name = 'books/book_list.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 1

    def get(self, request, *args, **kwargs):
        limit = request.GET.get('limit', 1)

        self.paginate_by = limit

        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['now'] = datetime.datetime.now()
        context['limit'] = self.paginate_by

        return context

class BookCreateView(CreateView):
    template_name = 'books/create.html'
    model = Book
    form_class = BookCreateForm
    success_url = reverse_lazy('list')

class BookDetailView(DetailView):
    template_name = 'books/detail.html'
    model = Book
    context_object_name = 'book'

class BookUpdateView(UpdateView):
    template_name = 'books/update.html'
    model = Book
    form_class = BookCreateForm
    success_url = reverse_lazy('list')

class BookDeleteView(DeleteView):
    template_name = 'books/delete.html'
    model = Book
    success_url = reverse_lazy('list')

