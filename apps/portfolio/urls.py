from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_list_view, name='list'),
    path('project/<int:pk>/', views.portfolio_detail_json_view, name='detail_json'),
]