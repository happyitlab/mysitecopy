from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index),
    path('', views.PostList.as_view()),
    # path('<int:pk>/', views.post_detail),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.PostListByCategory.as_view()),
    path('search/', views.Search.as_view()),
    path('search/<str:question>/', views.PostSearch.as_view()),
]
