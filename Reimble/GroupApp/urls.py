from django.urls import path, include

from .views import GroupModelView, GroupPostsView

urlpatterns = [
    path("groups/", GroupModelView.as_view()),
    path("group-posts/", GroupPostsView.as_view()),
]