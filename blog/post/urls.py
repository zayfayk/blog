from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView ,base, CategoryView

urlpatterns = [
    path('', base, name='base'),
    path('home/', HomeView.as_view(), name='Home'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post_update/<int:pk>/', UpdatePostView.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', DeletePostView.as_view(), name='post_delete'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
]