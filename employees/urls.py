from django.urls import path
from .views import EmployeeListView, EmployeesDetailView, EmployeesUpdateView, EmployeesDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/', views.update, name='update'),
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('employee/<int:pk>/', EmployeesDetailView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/update/', EmployeesUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', EmployeesDeleteView.as_view(), name='employee-delete'),

]
