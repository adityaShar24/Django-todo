from django.shortcuts import render , redirect
from ..models import Todo
from ..forms import TodoForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    tasks = Todo.objects.all()
    form = TodoForm()
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()     
        return redirect('/')
            
    
    context = {
        'tasks' : tasks,
        'form' : form
    }
    return render(request , 'TodoApp/list.html' , context)


@login_required(login_url='login')
def update_task(request , pk):
    task = Todo.objects.get(id=pk)
    
    form = TodoForm(instance=task)
    
    if request.method == 'POST':
        form = TodoForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form' : form
    }
    return render(request , 'TodoApp/update_task.html' , context)

@login_required(login_url='login')
def delete_task(request , pk):
    item = Todo.objects.get(id=pk)
    context = {
        'item' : item
    }
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    return render(request , 'TodoApp/delete.html' , context)
