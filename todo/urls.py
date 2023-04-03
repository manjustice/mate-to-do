from django.urls import path

from .views import (
    index,
    update_is_done,
    TagListView,
    CreateTaskView,
    UpdateTaskView,
    DeleteTaskView,
    CreateTagView,
    UpdateTagView,
    DeleteTagView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags", TagListView.as_view(), name="tags"),
    path("task/create", CreateTaskView.as_view(), name="add-task"),
    path("task/<int:pk>/update", UpdateTaskView.as_view(), name="update-task"),
    path("task/<int:pk>", DeleteTaskView.as_view(), name="delete-task"),
    path("task/<int:pk>/update-is-done", update_is_done, name="update-is-done"),
    path("tag/create", CreateTagView.as_view(), name="add-tag"),
    path("tag/<int:pk>/update", UpdateTagView.as_view(), name="update-tag"),
    path("tag/<int:pk>/delete", DeleteTagView.as_view(), name="delete-tag"),
]

app_name = "todo"
