from django.contrib.auth import login
from django.shortcuts import render, redirect
from worklist.models import Task
from worklist.forms import UserCreationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически входить в систему после регистрации
            return redirect('mainPage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def mainPage(request):
    if request.method == 'POST':
        title_req = request.POST['title']
        description_req = request.POST['description']
        deadline_req = request.POST['deadline']

        task = Task(title=title_req, description=description_req, deadline=deadline_req)
        task.save()
    else:
        print('Error')
    tasks = Task.objects.all()  # Получение всех задач из базы данных
    context = {'tasks': tasks}  # Передача задач в контекст
    return render(request, 'index.html', context)
