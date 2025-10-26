from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('reviews/', views.reviews_view, name='reviews'),
    path('submit-form/', views.submit_form_view, name='submit_form'),
]