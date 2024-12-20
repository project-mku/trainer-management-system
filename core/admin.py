from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Trainer,TrainerSkills, Payroll, PaymentMethod, Course, Schedule, Student, Enrollment, Feedback, Manager,ManagerAuthenticationCodes, Payslip, SchoolAccount, Deductions, Allowances, Report

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_trainer', 'is_manager',)
    list_filter = ('is_trainer', 'is_manager', 'is_staff',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_trainer', 'is_manager')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_trainer', 'is_manager')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Trainer),
admin.site.register(TrainerSkills)
admin.site.register(Payroll)
admin.site.register(PaymentMethod)
admin.site.register(Course)
admin.site.register(Schedule)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Feedback)
admin.site.register(Payslip)
admin.site.register(SchoolAccount)
admin.site.register(Manager)
admin.site.register(ManagerAuthenticationCodes)
admin.site.register(Deductions)
admin.site.register(Allowances)
admin.site.register(Report)
