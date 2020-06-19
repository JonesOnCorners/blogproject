from django.urls import path
from blog.views import (index, 
                        PostListView, 
                        PostDetailView, 
                        PostCreateView, 
                        PostUpdateView, 
                        PostDeleteView
)



urlpatterns = [
    path('',PostListView.as_view(),name='index'),
    path('post/create/',PostCreateView.as_view(),name='post-create'),
    path('post/<str:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<str:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<str:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
]