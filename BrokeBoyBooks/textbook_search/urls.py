from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addTextbook', views.addTextbook, name='addTextbook'),
    path('displayTextbook', views.displayTextbook, name='displayTextbook')
]
