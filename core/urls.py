from django.urls import path
from . import views

urlpatterns = [
    # auth views
    path('login/', views.account_login, name='account_login'),
    path('register/', views.register, name='register'),
    path('set_account_role/', views.set_account_role, name='set_account_role'),
    path('authenticate_manager/', views.authenticate_manager, name='authenticate_manager'),

    path('', views.index, name="index"),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('manager_dashboard/manage_users', views.user_management, name='user_management'),
    path('manager_dashboard/manage_users/<int:user_id>/', views.user_details, name='user_details'),
    path('manager_dashboard/manage_users/<int:user_id>/delete/', views.delete_user, name='delete_user'),

    # manager dashboard views ---> accounts
    path('manager_dashboard/accounts', views.accounts, name='manager_dashboard_accounts'),
    path('manager_dashboard/accounts/update/', views.manager_update, name='manager_update'), 
    path('manager_dashboard/accounts/<int:account_id>', views.account_details, name='account_details'),
    path('manager_dashboard/accounts/<int:account_id>/delete/', views.delete_account, name='delete_account'),
    path('manager_dashboard/trainers_management/', views.trainers_management, name='manage_trainers'),

    path('manager_dashboard/settings/', views.manager_settings, name='manager_settings'),

    # Payment views
    path('manager_dashboard/payments', views.payroll, name='manager_dashboard_payroll'),

    # Trainer views
    path('trainer_dashboard/', views.trainers_management, name='trainers_management'),
    path('trainer_dashboard/update_details/<int:pk>/', views.update_trainer_details, name='update_trainer_details'),
    


    # Reports views
    path('manager_dashboard/reports/', views.reports, name='reports'),


    path('about/', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact_us')
]
