from django.urls import path
from . import views

urlpatterns = [
    # auth views
    path('login/', views.account_login, name='account_login'),
    path('register/', views.register, name='register'),
    path('set_account_role/', views.set_account_role, name='set_account_role'),

    path('', views.index, name="index"),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('trainer_dashboard/', views.trainer_dashboard, name='trainer_dashboard'),
    path('about/', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact_us')
]
