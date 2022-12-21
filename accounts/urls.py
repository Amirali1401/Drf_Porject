from django.urls import path

from . import views as accounts_views

urlpatterns = [
    path('register/',accounts_views.Register.as_view() , name='register'),
    ]