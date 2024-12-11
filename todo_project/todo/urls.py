from django.urls import path
from .views import add_item
from . import views
from .views import delete_item

urlpatterns = [
    path("todo/", views.TodoListView.as_view()),
    path("todo/add/", add_item),
    path("todo/delete/<int:item>", delete_item),
]