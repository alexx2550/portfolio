from django.urls import path
from . import views


app_name = 'developers'
urlpatterns = [
    path('', views.ProgrammerListView.as_view(), name='programmer_list'),
    path('programmer/<int:pk>/', views.ProgrammerDetailView.as_view(), name='programmer_detail'),
    path('add_programmer/', views.ProgrammerCreateView.as_view(), name='add_programmer'),
    path('programmer/<int:pk>/add_project/', views.ProjectCreateView.as_view(), name='add_project'),
]

