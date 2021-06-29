from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    # tasks = Task.objects.all()
    # tasks = Task.objects.order_by('-id')
    tasks = Task.objects.order_by('deadline')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'tasks': tasks
                                               })


def about(request):
    return render(request, 'main/about-us.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма задана неверно'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
