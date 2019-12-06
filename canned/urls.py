from django.urls import path

from . import views

app_name = 'canned'
urlpatterns = [
    # ex: /canned/
    path('', views.index, name='index'),
]