from django.urls import path

from .views import index, TagListView

urlpatterns = [
    path("", index, name="index"),
    path("tags", TagListView.as_view(), name="tags"),
]

app_name = "todo"
