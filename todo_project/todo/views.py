from .models import TodoListItem
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

def add_item(request):
    if request.method == 'POST':
        text = request.POST.get("content")
        new_item = TodoListItem(content=text)
        new_item.save()
        return HttpResponseRedirect(redirect_to="todo/")
    return render(request, 'index.html')

def delete_item(request, item):
    obj = TodoListItem.objects.get(pk=item)
    obj.delete()
    return HttpResponseRedirect(redirect_to="todo/")

class TodoListView(ListView):
    model = TodoListItem
    template_name = "index.html"