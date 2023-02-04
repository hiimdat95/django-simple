
from django.urls import include, path, re_path
from posts.views import (
    ListPostView,
    CreatePostView,
)

urlpatterns = [
    re_path(r'^list-posts/$', ListPostView.as_view(), name='list-posts'),
    re_path(r'^create-post/$', CreatePostView.as_view(), name='create-post'),
]
# urlpatterns = [
#     path('list-posts/', ListPostView.as_view(), name='list-posts'),
#     path('create-posts/', CreatePostView.as_view(), name='create-posts'),
# ]
