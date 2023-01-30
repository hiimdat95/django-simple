
from django.conf.urls import url
from posts.views import (
    ListPostView,
    CreatePostView,
)

urlpatterns = [
    url(r'^list-posts/$', ListPostView.as_view(), name='list-posts'),
    url(r'^create-post/$', CreatePostView.as_view(), name='create-post'),
]
# urlpatterns = [
#     path('list-posts/', ListPostView.as_view(), name='list-posts'),
#     path('create-posts/', CreatePostView.as_view(), name='create-posts'),
# ]
