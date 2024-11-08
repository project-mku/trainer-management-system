from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from  django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from core.models import ManagerAuthenticationCodes, SchoolAccount, Payroll, Manager, Trainer, CustomUser, TrainerSkills
from .forms import CustomUserCreationForm, CustomUserUpdateForm, ManageUpdateForm, SchoolAccountUpdateForm, SchoolAccountAddForm, TrainerUpdateAdminForm, TrainerUpdateForm, TrainerAddForm, PayTrainerForm, AddTrainerSkillsForm, AddPayRoll, UpdatePayrollForm
from django.contrib import messages


# helper function to get the correct dashboard URL based on the user's role
def get_dashboard_url(user):
    """Return the correct dashboard URL based on the user's role."""

    if user.is_trainer:
        return 'trainer_dashboard'
    elif user.is_manager:
        return 'manager_dashboard'
    else:
        return 'set_account_role'

def account_login(request):
    if request.user.is_authenticated:
        return redirect(get_dashboard_url(request.user))
    
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email', '')
        password = request.POST.get('password', '')

        # Initialize user as None
        user = None
        
        # Check if logging in with email or username
        if '@' in username_or_email:
            # Email-based login
            user = authenticate(email=username_or_email, password=password)
        else:
            # Username-based login
            user = authenticate(username=username_or_email, password=password)

        # If user is authenticated
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully')

            # Redirect based on role
            if user.is_manager:
                return redirect('manager_dashboard')
            elif user.is_trainer:
                return redirect('trainer_dashboard')
            else:
                return redirect('set_account_role')
        else:
            messages.error(request, 'Invalid email/username or password')
            return redirect('account_login')

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

@login_required
def set_account_role(request):

    user = request.user

    if user.is_trainer:
        return redirect('trainer_dashboard')
    elif user.is_manager:
        return redirect('manager_dashboard')
    
    if request.method == 'POST':
        role = request.POST.get('role')

        if role == 'trainer':
            request.user.is_trainer = True
            request.user.save()

            # Create a trainer object
            trainer = Trainer.objects.create(user=request.user, email=request.user.email)
            trainer.save()

            messages.success(request, 'You are now a trainer')
            return redirect('trainer_dashboard')
        
        elif role == 'manager':
            
            request.user.is_temp_manager = True
            request.user.save()  # Save the temporary status in the database

            messages.info(request, 'Please authenticate to become a manager')
            return redirect('authenticate_manager')

        else:   
            return redirect('set_account_role')
        

    return render(request, 'registration/set_account_role.html')

@login_required
def authenticate_manager(request):
    system_codes = list(ManagerAuthenticationCodes.objects.values_list('code', flat=True))
    print(system_codes)

    if request.method == 'POST':
        code = request.POST.get('code')
        if code in system_codes:
            request.user.is_temp_manager = False
            request.user.is_manager = True
            request.user.save()

            # Create a manager object
            manager = Manager.objects.create(user=request.user)
            manager.save()

            messages.success(request, 'Authentication successful. You are now a manager')
            return redirect('manager_dashboard')
        else:
            messages.error(request, 'Authentication failed')
            return redirect('authenticate_manager')

    return render(request, 'registration/authenticate_manager.html')

def index(request):

    return render(request, 'core/index.html')


# ============================= Manager Dashboard Area =============================
@login_required
def manager_dashboard(request):

    manager = Manager.objects.get(user=request.user)
    if not manager.is_updated:
        messages.error(request, 'Please update your details first')
        return redirect('manager_update')
    
    return render(request, 'core/manager_dashboard.html')

@login_required
def manager_update(request):
    update_form = ManageUpdateForm()
    manager = Manager.objects.get(user=request.user)

    if request.method == 'POST':
        update_form = ManageUpdateForm(request.POST, instance=manager)
        if update_form.is_valid():
            update_form.save()
            manager.is_updated = True
            manager.save()
            messages.success(request, 'Manager details updated successfully')
            return redirect('manager_dashboard')
        else:
            messages.error(request, 'Manager details update failed')
            return redirect('manager_update')
    else:
        update_form = ManageUpdateForm(instance=manager)

    context = {
        'update_form': update_form
    }

    return render(request, 'core/management/manager_update.html', context)

@login_required
def user_management(request):
    manager = Manager.objects.get(user=request.user)

    if not manager.is_updated:
        messages.error(request, 'Please update your details first')
        return redirect('manager_update')
    users = CustomUser.objects.all().order_by('-date_joined')
    add_user_form = CustomUserCreationForm()

    if request.method == 'POST':
        add_user_form = CustomUserCreationForm(request.POST)
        if add_user_form.is_valid():
            add_user_form.save()
            messages.success(request, 'User added successfully')
            return redirect('user_management')
        else:
            messages.error(request, 'User add failed')
            return redirect('user_management')
    else:
        add_user_form = CustomUserCreationForm()

    context = {
        'add_user_form': add_user_form,
        'users': users
    }
    
    return render(request, 'core/management/user_management.html', context)

@login_required
def user_details(request, user_id):
    
    manager = Manager.objects.get(user=request.user)
    if not manager.is_updated:
        messages.error(request, 'Please update your details first')
        return redirect('manager_update')
    
    user = CustomUser.objects.get(id=user_id)
    update_form = CustomUserUpdateForm(instance=user)

    if request.method == 'POST':
        update_form = CustomUserUpdateForm(request.POST, instance=user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'User updated successfully')
            return redirect('user_details', user_id=user.id)
        
        else:
            messages.error(request, 'User update failed')
            return redirect('user_details', user_id=user.id)
    
    else:
        update_form = CustomUserUpdateForm(instance=user)

    context = {
        'user': user,
        'form': update_form
    }

    return render(request, 'core/management/user_details.html', context)

@login_required
def delete_user(request, user_id):
    manager = Manager.objects.get(user=request.user)

    if not manager.is_updated:
        messages.error(request, 'Please update your details first')
        return redirect('manager_update')
    
    user = CustomUser.objects.get(id=user_id)

    user.delete()
    messages.success(request, 'User deleted successfully')

    return redirect('user_management')

@login_required
def accounts(request):
    manager = Manager.objects.get(user=request.user)
    if not manager.is_updated:
        messages.error(request, 'Please update your details first')
        return redirect('manager_update')
    
    acccounts = SchoolAccount.objects.all()
    add_form = SchoolAccountAddForm()

    if request.method == 'POST':
        add_form = SchoolAccountAddForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, 'Account added successfully')
            return redirect('manager_dashboard_accounts')
        else:
            messages.error(request, 'Account add failed')
            return redirect('manager_dashboard_accounts')
    else:
        add_form = SchoolAccountAddForm()


    context = {
        'accounts': acccounts,
        'form': add_form
    }
    
    return render(request, 'core/management/accounts.html', context)

@login_required
def account_details(request, account_id):
    manager = Manager.objects.get(user=request.user)
    if not manager.is_updated:
        messages.error(request, 'Please update your details first')
        return redirect('manager_update')
    
    account = SchoolAccount.objects.get(id=account_id)
    update_form = SchoolAccountUpdateForm(instance=account)

    if request.method == 'POST':
        update_form = SchoolAccountUpdateForm(request.POST, instance=account)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Account updated successfully')
            return redirect('account_details', account_id=account.id)
        
        else:
            messages.error(request, 'Account update failed')
            return redirect('account_details', account_id=account.id)
    
    else:
        update_form = SchoolAccountUpdateForm(instance=account)

    context = {
        'account': account,
        'form': update_form
    }

    return render(request, 'core/management/account_details.html', context)

@login_required
def delete_account(request, account_id):
    manager = Manager.objects.get(user=request.user)

    if not manager.is_updated:
        messages.error(request, 'Please update your details first')
        return redirect('manager_update')
    
    account = SchoolAccount.objects.get(id=account_id)
    account.delete()
    messages.success(request, 'Account deleted successfully')
    return redirect('manager_dashboard_accounts')

@login_required
def trainers_management(request):
    manager = Manager.objects.get(user=request.user)
    if not manager.is_updated:
        messages.error(request, 'Please update your details first')
        return redirect('manager_update')
    
    trainers = Trainer.objects.all()
    trainer_form = TrainerAddForm()

    if request.method == 'POST':
        trainer_form = TrainerAddForm(request.POST)
        if trainer_form.is_valid():
            trainer_form.save()
            messages.success(request, 'Trainer added successfully')
            return redirect('manage_trainers')
        else:
            messages.error(request, 'Trainer add failed')
            return redirect('manage_trainers')
    else:
        trainer_form = TrainerAddForm()
    

    context = {
        'trainers': trainers,
        'trainer_form': trainer_form
    }



    return render(request, 'core/management/trainers.html', context)

def trainer_details(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)

    trainer_form = TrainerUpdateAdminForm(instance=trainer)
    
    if request.method == 'POST':
        trainer_form = TrainerUpdateAdminForm(request.POST, instance=trainer)
        if trainer_form.is_valid():
            trainer_form.save()
            messages.success(request, 'Trainer details updated successfully')
            return redirect('trainer_details', trainer_id=trainer.id)
        else:
            messages.error(request, 'Trainer details update failed')
            return redirect('trainer_details', trainer_id=trainer.id)
    else:
        trainer_form = TrainerUpdateAdminForm(instance=trainer)

    context = {
        'trainer': trainer,
        'form': trainer_form
    }

    return render(request, 'core/management/trainer_details.html', context)

def delete_trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    trainer.delete()
    messages.success(request, 'Trainer deleted successfully')
    return redirect('manage_trainers')


# ============================= End of Manager Dashboard Area =============================

# ============================= Payroll Management =============================
@login_required
def payroll(request):
    manager = Manager.objects.get(user=request.user)

    if not manager.is_updated:
        messages.error(request, 'Please update your details first')
        return redirect('manager_update')
    
    payrolls = Payroll.objects.filter(trainer__on_payroll=True)

    add_payroll_form = AddPayRoll()
    
    if request.method == 'POST':
        add_payroll_form = AddPayRoll(request.POST)
        if add_payroll_form.is_valid():
            add_payroll_form.save()
            messages.success(request, 'Payroll added successfully')
            return redirect('manager_dashboard_payroll')
        else:
            messages.error(request, 'Payroll add failed')
            return redirect('manager_dashboard_payroll')
    else:
        add_payroll_form = AddPayRoll()
        

    context = {
        'payrolls': payrolls,
        'form': add_payroll_form
    }

    return render(request, 'core/management/payroll.html', context)


def payment_details(request, payment_id):
    payroll = Payroll.objects.get(id=payment_id)

    form = UpdatePayrollForm(instance=payroll)

    if request.method == 'POST':
        form = UpdatePayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payroll updated successfully')
            return redirect('payment_details', payment_id=payroll.id)
        else:
            messages.error(request, 'Payroll update failed')
            return redirect('payment_details', payment_id=payroll.id)
    else:
        form = UpdatePayrollForm(instance=payroll)

    contecxt = {
        'payroll': payroll,
        'form': form
    }


    return render(request, 'core/management/payroll_details.html', contecxt)

# ============================= End of Payroll Management =============================
@login_required
def trainer_dashboard(request):
    try:
        trainer = Trainer.objects.get(user=request.user)
    except Trainer.DoesNotExist:
        messages.error(request, 'You are not a trainer, please contact the system admin')
        return redirect('account_login')

    if not trainer.account_updated:
        return redirect('update_trainer_details', pk=trainer.id)
    
    context = {
        'trainer': trainer
    }

    return render(request, 'core/trainer_dashboard.html', context)

@login_required
def update_trainer_details(request, pk):

    try:
        trainer = Trainer.objects.get(pk=pk)
    except Trainer.DoesNotExist:
        messages.error(request, 'Trainer not found')
        return redirect('trainer_dashboard')

    update_trainer_form = TrainerUpdateForm()
    
    
    if request.method == 'POST':
        update_trainer_form = TrainerUpdateForm(request.POST,request.FILES, instance=trainer)
        if update_trainer_form.is_valid():
            trainer.account_updated = True
            trainer.save()
            update_trainer_form.save()
            messages.success(request, 'Trainer details updated successfully')
            return redirect('trainer_dashboard')
        else:
            messages.error(request, 'Trainer details update failed')
            return redirect('update_trainer_details', pk=trainer.id)
    else:
        update_trainer_form = TrainerUpdateForm(instance=trainer)

    context = {
        'form': update_trainer_form,
        'trainer': trainer,
    }

    return render(request, 'core/trainer/update_trainer_details.html', context)

def set_trainer_skills(request, pk):
    try :
        trainer = Trainer.objects.get(pk=pk)
        
    except Trainer.DoesNotExist:
        messages.error(request, 'Trainer not found')
        return redirect('trainer_dashboard')

    set_skills_form = AddTrainerSkillsForm()
    skills = TrainerSkills.objects.filter(trainer=trainer).order_by('-created')

    if request.method == 'POST':
        set_skills_form = AddTrainerSkillsForm(request.POST)
        if set_skills_form.is_valid():
            trainer_skills = set_skills_form.save(commit=False)
            trainer_skills.trainer = trainer
            trainer_skills.save()
            messages.success(request, 'Skills updated successfully')
           
    else:
        set_skills_form = AddTrainerSkillsForm()

    context = {
        'form': set_skills_form,
        'trainer': trainer,
        'skills': skills
    }


    return render(request, 'core/trainer/set_skills.html', context)

def add_skills(request, pk):
    try:
        trainer = Trainer.objects.get(pk=pk)
    except Trainer.DoesNotExist:
        messages.error(request, 'You are not a trainer, please contact the system admin')
        return redirect('account_login')
    
    if request.method == 'POST':
        skill = request.POST.get('skill')
        TrainerSkills.objects.create(trainer=trainer, skill=skill)
        messages.success(request, 'Skill added successfully')
    
    skills = TrainerSkills.objects.filter(trainer=trainer)

    context = {
        'skills': skills,
        'trainer': trainer
    }
    
    return render(request, 'core/trainer/partials/add_skills.html', context)

@csrf_exempt
@login_required
def delete_skill(request, pk):
    try:
        skill = get_object_or_404(TrainerSkills, pk=pk)
        skill.delete()
        messages.success(request, 'Skill deleted successfully')
    except TrainerSkills.DoesNotExist:
        messages.error(request, 'Skill not found')
    
    skills = TrainerSkills.objects.all()

    context = {
        'skills': skills,
        # 'trainer': trainer
    }
    
    return render(request, 'core/trainer/partials/add_skills.html', context)


@login_required
def manager_settings(request):
    return render(request, 'core/management/settings.html')

@login_required
def reports(request):
    
        return render(request, 'core/management/reports.html')



def trainer_assignments(request):
    trainer = Trainer.objects.get(user=request.user)
    return render(request, 'core/trainer/assignments.html', {'trainer':trainer})

def trainer_schedules(request):
    trainer = Trainer.objects.get(user=request.user)
    return render(request, 'core/trainer/schedules.html', {'trainer':trainer})

def trainer_grades(request):
    trainer = Trainer.objects.get(user=request.user)
    return render(request, 'core/trainer/grades.html', {'trainer':trainer})

def trainer_reports(request):
    trainer = Trainer.objects.get(user=request.user)

    return render(request, 'core/trainer/reports.html', {'trainer':trainer})

def trainer_settings(request):
    trainer = Trainer.objects.get(user=request.user)
    return render(request, 'core/trainer/settings.html', {'trainer':trainer})


@login_required
def about(request):

    return render(request, 'core/about.html')

@login_required
def contact_us(request):
    
    return render(request, 'core/contact_us.html')