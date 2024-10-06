from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, SchoolAccount, Trainer, Manager

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

class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = [
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


