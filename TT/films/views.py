from django.shortcuts import render, redirect
from .forms import MovieForm
from django.shortcuts import render
from .models import Movie

# Create your views here.

def ttr (request):
    movies = Movie.objects.all()
    return render(request , 'films/inform.html' , {'movies': movies})


def rrt(request):
    if request.method == 'POST':
        # Если форма отправлена (POST-запрос), обрабатываем данные
        form = MovieForm(request.POST)
        if form.is_valid():

            form.save()  # Сохраняем данные в базу данных
            return redirect('info')  # Перенаправляем на страницу успеха
    else:
        # Если это GET-запрос, показываем пустую форму
        form = MovieForm()

    return render(request, 'films/vvod.html' ,  {'form': form })

