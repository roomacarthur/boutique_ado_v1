from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home') #root url to render index view.
]
