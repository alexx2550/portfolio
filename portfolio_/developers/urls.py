from django.urls import path
from . import views

app_name = 'developers'

urlpatterns = [
    path('', views.developer_list, name='developer_list'),
    path('add/', views.add_developer, name='add_developer'),
    path('<int:pk>/', views.developer_detail, name='developer_detail'),
]
