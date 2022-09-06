from django.urls import path, include
from . import views
import articles

app_name=articles
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create')
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('post/', views.post, name='post'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>', views.update, name='update'),
]