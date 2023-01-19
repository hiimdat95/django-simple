
from django.urls import path
from django.contrib import admin
from posts.views import (
    ListPostView,
    CreatePostView,
)

# urlpatterns = [
#     path(r'^list-posts/$', ListPostView.as_view(), name='list-posts'),
#     path(r'^create-post/$', CreatePostView.as_view(), name='create-post'),
# ]
urlpatterns = [
    path('list-posts/', ListPostView.as_view(), name='list-posts'),
    path('create-posts/', CreatePostView.as_view(), name='create-posts'),
]
