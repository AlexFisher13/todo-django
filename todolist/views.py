from django.shortcuts import render

from todos.models import Task


def main_page(request):
    task_text = request.POST.get('new_task_text', 'new task')
    new_task = Task(text=task_text, is_done=False)
    new_task.save()
    tasks = Task.objects.all()
    return render(request, './index.html', {
        'text': 'Список заданий',
        'tasks': tasks
    })
