from django.urls import path
from . import views

#setting this app name. app_name variable name is a known varible which django knows
app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
