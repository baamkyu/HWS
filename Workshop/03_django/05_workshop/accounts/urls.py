from django.urls import path, include
from . import views

app_name='accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup')
]

