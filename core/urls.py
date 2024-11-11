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
    path('manager_dashboard/trainers_management/', views.trainers_management, name='trainers_management'),
    path('manager_dashboard/trainers_management/<int:trainer_id>/', views.trainer_details, name='trainer_details'),
    path('manager_dashboard/trainers_management/<int:trainer_id>/delete/', views.delete_trainer, name='delete_trainer'),
    path('manager_dashboard/trainers_management/get_trainer_payroll_details/', views.get_trainer_payroll_details, name='get_trainer_payroll_details'),
    path('manager_dashboard/trainers_management/calculate_hourly_payroll/<int:trainer_id>/', views.calculate_payroll_hourly, name='calculate_hourly_payroll'),

    path('manager_dashboard/settings/', views.manager_settings, name='manager_settings'),

    # Payment views
    path('manager_dashboard/payments', views.payroll, name='manager_dashboard_payroll'),
    path('manager_dashboard/payments/<int:payment_id>/', views.payment_details, name='payment_details'),
    path('manager_dashboard/payments/pay_none_payroll/', views.pay_none_payroll, name='pay_none_payroll'),

    path("manager_dashboard/payments/get_none_payroll/", views.get_non_payroll_trainers, name="get_non_payroll_trainers"),
    path("manager_dashboard/payments/get_payroll/", views.get_payroll_trainers, name="get_payroll_trainers"),
    path("manager_dashboard/payments/manage_trainer_payslip/<int:payroll_id>/", views.manage_trainer_payslip, name="manage_trainer_payslip"),

    # Trainer views
    path('trainer_dashboard/', views.trainer_dashboard, name='trainer_dashboard'),
    path('trainer_dashboard/update_details/<int:pk>/', views.update_trainer_details, name='update_trainer_details'),
    path('trainer_dashboard/set_skill/<int:pk>/', views.set_trainer_skills, name='set_skill'),
    path('trainer_dashboard/add_skill/<int:pk>/', views.add_skills, name='add_skills'),
    path('trainer_dashboard/delete_skill/<int:pk>/', views.delete_skill, name='delete_skill'),
    path('trainer_dashboard/payslip/', views.trainer_payslip, name='trainer_payslip'),
    path('trainer_dashboard/payslip/details/<int:payslip_id>/', views.trainer_payslip_details, name='trainer_payslip_details'),

    path('trainer_dashboard/settings/', views.trainer_settings, name='trainer_settings'),





    


    # Reports views
    path('manager_dashboard/reports/', views.reports, name='reports'),
    path('manager_dashboard/reports/details/<int:report_id>/', views.report_details, name='report_details'),
    path('manager_dashboard/reports/delete/<int:report_id>/', views.delete_report, name='delete_report'),


    path('about/', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact_us')
]
