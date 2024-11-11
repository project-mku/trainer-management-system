from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Report, SchoolAccount, Trainer, Manager, Payroll, TrainerSkills
from django.core.exceptions import ValidationError
from datetime import date

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'gender', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring focus:ring-blue-500',
                'placeholder': 'Enter your username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring focus:ring-blue-500',
                'placeholder': 'Enter your email',
            }),

            'gender': forms.Select(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring focus:ring-blue-500',
            }),

            'password1': forms.PasswordInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring focus:ring-blue-500',
                'placeholder': 'Enter your password',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring focus:ring-blue-500',
                'placeholder': 'Confirm your password',
            }),
        }

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email','first_name','last_name','date_joined','last_login','is_active','is_staff']

class SchoolAccountAddForm(forms.ModelForm):
    class Meta:
        model = SchoolAccount
        fields = [
            'bank_name',
            'account_number',
            'branch_code',
            'branch',
            'total_balance',
        ]
        widgets = {
            'bank_name': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300'
            }),
            'account_number': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300'
            }),
            'branch_code': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300'
            }),
            'branch': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300'
            }),
            'total_balance': forms.NumberInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300'
            }),
        }

class SchoolAccountUpdateForm(forms.ModelForm):
    class Meta:
        model = SchoolAccount
        fields = [
            'bank_name',
            'account_number',
            'branch_code',
            'branch',
            'total_balance',
        ]
        widgets = {
            'bank_name': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300'
            }),
            'account_number': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300'
            }),
            'branch_code': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300'
            }),
            'branch': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300'
            }),
            'total_balance': forms.NumberInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300'
            }),
        }

class TrainerUpdateAdminForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'id_number', 
            'phone_number', 
            'bio', 
            'years_of_experience',
            'profile_picture', 
            'department', 
            'salary_type', 
            'base_salary',
            'on_payroll',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'First Name'}),
            
            'last_name': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Last Name'}),
            
            'email': forms.EmailInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Email'}),
            
            'id_number': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'ID Number'}),
            
            'phone_number': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Phone Number'}),
            
            'bio': forms.Textarea(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Bio', 'rows': 3}),

            'years_of_experience': forms.NumberInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Years of Experience'}),
            
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm'}),
            
            'department': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Department'}),

            'salary_type': forms.Select(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),

            'base_salary': forms.NumberInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Base Salary'}),

            'on_payroll': forms.CheckboxInput(attrs={'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}),
            
        }

class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = [
            'profile_picture', 
            'first_name', 
            'last_name', 
            'email', 
            'id_number', 
            'phone_number', 
            'bio', 
            'years_of_experience',
            # 'department', 
            # 'salary_type', 
        ]
        widgets = {

            'profile_picture': forms.ClearableFileInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm'}),

            'first_name': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'First Name'}),
            
            'last_name': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Last Name'}),
            
            'email': forms.EmailInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Email'}),
            
            'id_number': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'ID Number'}),
            
            'phone_number': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Phone Number'}),
            
            'bio': forms.Textarea(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Bio', 'rows': 3}),

            'years_of_experience': forms.NumberInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Years of Experience'}),
            
            
            # 'department': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Department'}),

            # 'salary_type': forms.Select(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),

        }

class TrainerAddForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = [
            'user',
            'first_name', 
            'last_name', 
            'email', 
            'id_number', 
            'phone_number', 
            'bio', 
            'profile_picture', 
            'department', 
            'salary_type', 
        ]
        widgets = {
            'user' : forms.Select(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}), 

            'first_name': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'First Name'}),
            
            'last_name': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Last Name'}),
            
            'email': forms.EmailInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Email'}),
            
            'id_number': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'ID Number'}),
            
            'phone_number': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Phone Number'}),
            
            'bio': forms.Textarea(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Bio', 'rows': 3}),
            
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm'}),

            'department': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Department'}),

            'salary_type': forms.Select(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),

        }
    
class ManageUpdateForm(forms.ModelForm):
    class Meta:
        model = Manager

        fields = [
            'id_number',
            'phone_number',
            'address',
            # 'role',
        ]

        widgets = {
            'id_number': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'ID Number'}),
            
            'phone_number': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Phone Number'}),
            
            'address': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Address'}),
            
            'role': forms.Select(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),
        }

class PreparePayrollForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['base_salary']

        widgets = {
            'base_salary': forms.NumberInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),
        }

class PrepareNonePayrollForm(forms.ModelForm):

    class Meta:
        model = Trainer
        fields = ['hours_worked', 'hourly_rate', 'base_salary']

        widgets = {
            'hours_worked': forms.NumberInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),
            'base_salary': forms.NumberInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),

        }

class AddPayRoll(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = [  
            'month', 
            'pay_period_start', 
            'pay_period_end', 
            'payment_date',
        ]
        widgets = {
            
            'month': forms.Select(
                attrs={
                    'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'
                    }
                ),
            'pay_period_start': forms.DateInput(
                attrs={
                    'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500',
                    'type' : 'date'
                    }
                ),

            'pay_period_end': forms.DateInput(
                attrs={
                    'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500',
                    'type' : 'date'
                    }
                ),

            'payment_date': forms.DateInput(
                attrs={
                    'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500',
                    'type': 'date',
                    'max': date.today()
                    }
                ),
        }

    def clean_pay_period_start(self):
        pay_period_start = self.cleaned_data["pay_period_start"]
        
        # Additional validation logic (if necessary)
        if pay_period_start > date.today():
            raise ValidationError("The pay period start cannot be in the future.")
        
        return pay_period_start

    def clean_pay_period_end(self):
        pay_period_end = self.cleaned_data["pay_period_end"]
        pay_period_start = self.cleaned_data.get("pay_period_start")
        
        if pay_period_start and pay_period_end < pay_period_start:
            raise ValidationError("The pay period end cannot be before the pay period start.")
        
        # Additional validation for future dates if necessary
        if pay_period_end > date.today():
            raise ValidationError("The pay period end cannot be in the future.")
        
        return pay_period_end

    def clean_hours_worked(self):
        hours_worked = self.cleaned_data["hours_worked"]
        
        # Ensure hours worked is a positive number
        if hours_worked < 0:
            raise ValidationError("Hours worked must be a positive number.")
        
        return hours_worked

    def clean_total_payment(self):
        total_payment = self.cleaned_data["total_payment"]
        hours_worked = self.cleaned_data.get("hours_worked")
        
        if hours_worked is not None and total_payment is not None:
            # Add custom validation to check if total_payment is reasonable
            expected_payment = hours_worked * 20  # Example: assuming 20 is the hourly rate
            if total_payment != expected_payment:
                raise ValidationError(f"The total payment should be {expected_payment} based on hours worked.")
        
        return total_payment

    def clean_payment_date(self):
        payment_date = self.cleaned_data["payment_date"]
        pay_period_end = self.cleaned_data.get("pay_period_end")
        
        if pay_period_end and payment_date > pay_period_end:
            raise ValidationError("The payment date cannot be after the pay period end date.")
        
        return payment_date

    def clean(self):
        cleaned_data = super().clean()
        
        # Custom form-wide validation
        pay_period_start = cleaned_data.get('pay_period_start')
        pay_period_end = cleaned_data.get('pay_period_end')

        if pay_period_start and pay_period_end:
            if pay_period_end < pay_period_start:
                self.add_error('pay_period_end', 'The pay period end cannot be before the pay period start.')

        return cleaned_data
        
class TrainersSelectForm(forms.Form):
    trainer = forms.ModelChoiceField(
        queryset=Trainer.objects.all(),
        empty_label="Select a trainer",
        widget=forms.Select(
            attrs={
                'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500',
                'name' : 'trainer',
                'hx-post': '/manager_dashboard/trainers_management/get_trainer_payroll_details/',
                'hx-target': '#trainer_details',
                'hx-trigger': 'change',
                }
            )
    )

class SelectSchoolAccountForm(forms.Form):
    account = forms.ModelChoiceField(
        label="Bank Account to pay Trainer",
        queryset=SchoolAccount.objects.all(),
        empty_label="Select an account to pay Trainer",
        widget=forms.Select(
            attrs={
                'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500',
                'name' : 'account',
                
                }
            )
    )

class AddTrainerSkillsForm(forms.ModelForm):
    class Meta:
        model = TrainerSkills
        fields = ['skill']
        widgets = {
            'skill': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Skill', 'name' : 'skill', 'required': True}),
        }

class UpdatePayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = [
            'trainer', 
            'month', 
            'pay_period_start', 
            'pay_period_end', 
            'hours_worked', 
            'total_payment', 
            'status',
            'payment_date',
            
        ]
        widgets = {
            'trainer': forms.Select(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}), 

            'month': forms.Select(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),

            'pay_period_start': forms.DateInput(
                attrs={
                    'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'
                    }
                ),

            'pay_period_end': forms.DateInput(
                attrs={
                    'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'
                       }
                ),

            'hours_worked': forms.NumberInput(
                attrs={
                    'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'
                       
                    }
                ),

            'total_payment': forms.NumberInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),

            'status': forms.Select(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),

            'payment_date': forms.DateInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500'}),

        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'mt-1 mb-4 block w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-500', 'placeholder': 'Description', 'rows': 15}),
        }

        
