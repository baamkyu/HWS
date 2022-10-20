<<<<<<< HEAD
from . import views
from django.urls import path

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    ]
=======
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
  path('', views.index, name='index'),
  path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  path('<int:pk>', views.detail, name='detail'),
  path('<int:pk>/delete', views.delete, name='delete'),
  path('<int:pk>/edit', views.edit, name='edit'),
  path('<int:pk>/update', views.update, name='update'),
]
>>>>>>> d91e101d9b9fccd0ec02132f6b839b5d2dcb06bf
