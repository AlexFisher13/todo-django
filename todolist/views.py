from django.shortcuts import render

from todos.models import Task


def main_page(request):
    tasks = Task.objects.all()
    return render(request, './index.html', {
        'text': 'Список заданий',
        'tasks': tasks
    })
