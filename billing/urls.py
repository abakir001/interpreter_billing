from django.urls import path
from . import views
urlpatterns = [
    path('', views.deposits_calls, name='deposits_calls'),
    path('deposits/', views.deposits, name='deposits'),
    path('calls/', views.calls, name='calls'),
    path('users/', views.users, name='users'),
    path('add_call/<int:pk>/', views.add_call, name='add_call'),
    path('add_call_form/<int:pk>/', views.add_call_form, name='add_call_form'),
    path('add_deposit/<int:pk>/', views.add_deposit, name='add_deposit'),
    path('add_deposit_form/<int:pk>/', views.add_deposit_form, name='add_deposit_form'),
]
