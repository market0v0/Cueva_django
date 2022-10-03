from . import views
from django.urls import path

app_name ='registration'

urlpatterns =[
    path('', views.HomeView.as_view(),name='index'), #127.0.0.1/registration/
    path('createStudent', views.RegisterStudent.as_view(), name='create_student'),
    path('createRoom', views.RegisterRoom.as_view(), name='create_room')
]