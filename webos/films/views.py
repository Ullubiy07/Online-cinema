from django.db.models import Q
from django.shortcuts import render, redirect
from .models import AllFilms
from .forms import AllFilmsForm
from django.views.generic import DetailView, UpdateView, DeleteView, View


# вытаскиваем значения из базы данных
def films_home(request):
    films = AllFilms.objects.all()
    return render(request, "films/films_home.html", {'films': films})


# динамичский url
class FilmsDetailView(DetailView):
    model = AllFilms
    template_name = 'films/details_view.html'
    context_object_name = 'my_film'


class FilmsUpdateView(UpdateView):
    model = AllFilms
    template_name = 'films/create.html'

    form_class = AllFilmsForm


class FilmsDeleteView(DeleteView):
    model = AllFilms
    success_url = '/films/'
    template_name = 'films/films_delete.html'


# загрузка и обработка формы
def create(request):
    error = ''
    if request.method == 'POST':
        form = AllFilmsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('films_home')
        else:
            error = 'Форма заполнена неверно'

    form = AllFilmsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'films/create.html', data)

