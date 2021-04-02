from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TodoList

# Create your views here.

def index(request):

    # quering all todos with the object manager
    item_list = TodoList.objects.order_by("-created_date")

    if request.method == "POST":
        title = request.POST["title"]

        todolist = TodoList(title=title)
        todolist.save()
        return redirect('todo') # for reloading the page
    
    data = {
        "item_list" : item_list,
    }
    
    return render(request, 'todo/todo.html', data)


def remove(request, item_id):
    item = TodoList.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Todo removed !!!")
    return redirect('todo')