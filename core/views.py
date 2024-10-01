from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib import messages

def get_dashboard_url(user):
    """Return the correct dashboard URL based on the user's role."""
    if user.is_trainer:
        return 'trainer_dashboard'
    elif user.is_manager:
        return 'manager_dashboard'
    else:
        return 'set_account_role'

def account_login(request):
    # if request.user.is_authenticated:
    #     return redirect(get_dashboard_url(request.user))
    
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        print(email, password)

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully')
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password')

    # If not a POST request or if authentication fails, render login page
    return render(request, 'registration/login.html')

def register(request):
    register_form = CustomUserCreationForm()
    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('account_login')
    else:
        register_form = CustomUserCreationForm()

    context = {
        'form': register_form
    }
        
    return render(request, 'registration/register.html', context)

def set_account_role(request):
    
   

    if request.method == 'POST':
        role = request.POST.get('role')

        if role == 'trainer':
            request.user.is_trainer = True
            request.user.save()
            messages.success(request, 'You are now a trainer')
            return redirect('trainer_dashboard')
        
        elif role == 'manager':
            request.user.is_manager = True
            request.user.save()
            messages.success(request, 'Your account has been updated successfully. You are now a manager')
            return redirect('manager_dashboard')
        else:
            return redirect('set_account_role')
        

    return render(request, 'registration/set_account_role.html')

def index(request):

    return render(request, 'core/index.html')

def manager_dashboard(request):

    

    
    return render(request, 'core/manager_dashboard.html')

def trainer_dashboard(request):

    return render(request, 'core/trainer_dashboard.html')

def about(request):

    return render(request, 'core/about.html')

def contact_us(request):
    
    return render(request, 'core/contact_us.html')