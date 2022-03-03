from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='trainer'),
    path('add_objection/', views.add_objection, name='add_objection'),
]
