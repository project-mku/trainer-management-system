from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Ensure the email is unique for superuser as well
        extra_fields.setdefault('is_trainer', False)  # Optional: depending on your logic
        extra_fields.setdefault('is_manager', False)   # Optional: depending on your logic

        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    '''Model definition for CustomUser.'''

    class GenderChoices(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        OTHER = 'other', 'Other'


    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GenderChoices, null=True, blank=True)
    is_trainer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_temp_manager = models.BooleanField(default=False)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        '''Meta definition for CustomUser.'''
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email  

class Trainer(models.Model):
    '''Model definition for Trainer.'''
    SALARY_TYPE_CHOICES = [
        ('fixed', 'Fixed Salary'),
        ('hourly', 'Hourly Rate'),
    ]

    STATUSCHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    id_number = models.CharField(max_length=10, blank=True, null=True)
    trainer_no = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True, help_text='A brief description about you as a trainer')
    years_of_experience = models.IntegerField(default=0, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='trainer_pics/', blank=True, null=True)
    trainer_status = models.CharField(max_length=10, choices=STATUSCHOICES, default='active')
    department = models.CharField(max_length=200, default="", null=True, blank=True)  # E.g., Python, Data Science, etc. -----> Can be the department which the trainer is in
    account_updated = models.BooleanField(default=False)
    
    # Payroll related fields
    salary_type = models.CharField(max_length=6, choices=SALARY_TYPE_CHOICES, default='fixed', help_text="How would you like to be paid?")
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # For fixed salary
    hours_worked = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # For hourly payments
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # For hourly payments
    on_payroll = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        '''Meta definition for Trainer.'''
        verbose_name = 'Trainer'
        verbose_name_plural = 'Trainers'
        indexes = [
            models.Index(fields=['first_name', 'last_name']),
        ]

    @property
    def payment_mode(self):
        return self.salary_type
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.department}'
    
    def save(self, *args, **kwargs):
        if self.salary_type == 'hourly':
            self.base_salary = int(self.hourly_rate * self.hours_worked)
        
        if not self.trainer_no:
            self.trainer_no = f'TR_{uuid.uuid4().hex[:6].upper()}'

        super().save(*args, **kwargs)

class TrainerSkills(models.Model):
    '''Model definition for TrainerSkills.'''
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        '''Meta definition for TrainerSkills.'''
        verbose_name = 'Trainer Skill'
        verbose_name_plural = 'Trainer Skills'
        ordering = ['-created']

    def __str__(self):
        return f'{self.skill} - {self.trainer}'

class Payroll(models.Model):
    """
    Store payment records for trainers, calculating payments based on 
    their salary type (fixed salary or hourly rate). For hourly-paid 
    trainers, the model will track the number of hours worked per pay 
    period.
    """
    class MonthChoices(models.TextChoices):
        JANUARY = 'january', 'January'
        FEBRUARY = 'february', 'February'
        MARCH = 'march', 'March'
        APRIL = 'april', 'April'
        MAY = 'may', 'May'
        JUNE = 'june', 'June'
        JULY = 'july', 'July'
        AUGUST = 'august', 'August'
        SEPTEMBER = 'september', 'September'
        OCTOBER = 'october', 'October'
        NOVEMBER = 'november', 'November'
        DECEMBER = 'december', 'December'

    PAYROLL_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]
    
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    month = models.CharField(max_length=10, choices=MonthChoices.choices, null=True, blank=True)
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # For hourly rate trainers
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=PAYROLL_STATUS_CHOICES, default='pending')
    payment_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Payroll'
        verbose_name_plural = 'Payrolls'

    def __str__(self):
        return f'Payroll for {self.trainer} ({self.pay_period_start} to {self.pay_period_end})'

    def calculate_total_payment(self):
        """Calculate the total payment based on the trainer's salary type."""
        if self.trainer.salary_type == 'fixed':
            return self.trainer.base_salary
        elif self.trainer.salary_type == 'hourly':
            return self.trainer.hourly_rate * self.hours_worked   

class PaymentMethod(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('bank', 'Bank Transfer'),
        ('mpesa', 'Mpesa'),
        ('check', 'Check'),
        ('cash', 'Cash'),
    ]
    
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=6, choices=PAYMENT_TYPE_CHOICES)
    bank_account_number = models.CharField(max_length=20, blank=True, null=True)  # For bank transfer
    mpesa_number = models.EmailField(blank=True, null=True, help_text="If the payment is made via Mpesa")  # For Mpesa payments

    class Meta:
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'
        indexes = [
            models.Index(fields=['trainer', 'payment_type']),
        ]
    
    def __str__(self):
        return f'{self.payment_type} for {self.trainer}'

class Course(models.Model):
    """
    This Table will define the courses trainers can manage or teach.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    duration = models.IntegerField(help_text="Duration in hours")
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        indexes = [
            models.Index(fields=['title', 'start_date']),
        ]

class Schedule(models.Model):
    """
    This model will keep track of the schedule for each course, including the time and location of each session.
    """

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
        indexes = [
            models.Index(fields=['course', 'date']),
        ]
    
    def __str__(self):
        return f'{self.course.title} on {self.date} at {self.time}'

    
    def __str__(self):
        return self.title

class Student(models.Model):
    """
    Keep track which students are participating in the courses
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    enrolled_courses = models.ManyToManyField(Course, through='Enrollment')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        indexes = [
            models.Index(fields=['first_name', 'last_name']),
        ]
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Enrollment(models.Model):
    """
    Keep track of students' enrollment in courses.
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        indexes = [
            models.Index(fields=['student', 'course']),
        ]
    
    def __str__(self):
        return f'{self.student} enrolled in {self.course.title}'

class Feedback(models.Model):
    """
    This will allow students to leave feedback for trainers or courses.
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        indexes = [
            models.Index(fields=['course', 'student']),
        ]
    
    def __str__(self):
        return f'Feedback for {self.course.title} by {self.student}'

class Manager(models.Model):

    '''Model definition for Manager.'''

    class Rankchoices(models.TextChoices):
        Manager = 'manager', 'Manager'
        Assistant_Manager = 'assistant_manager', 'Assistant Manager'
        Supervisor = 'supervisor', 'Supervisor'
        Director = 'director', 'Director'


    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, choices=Rankchoices.choices, default='manager')
    bio = models.TextField(null=True, blank=True)
    is_updated = models.BooleanField(default=False)

    class Meta:
        '''Meta definition for Manager.'''

        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'
        indexes = [
            models.Index(fields=['user', 'id_number']),
        ]

    def __str__(self):
        return self.user.username

class ManagerAuthenticationCodes(models.Model):
    '''Model definition for ManagerAuthenticationCodes.'''

    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        '''Meta definition for ManagerAuthenticationCodes.'''

        verbose_name = 'Manager AuthenticationCode'
        verbose_name_plural = 'Manager Authentication Codes'

    def __str__(self):
        return self.code

class Allowances(models.Model):
    """
    Represents allowances that may be added to a trainer's salary, such as bonuses, overtime, etc.
    """
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Allowance'
        verbose_name_plural = 'Allowances'

    def __str__(self):
        return f'{self.trainer.user.username} {self.name} - {self.amount}'

class Deductions(models.Model):
    """
    Represents deductions that may be applied to a trainer's salary, such as taxes, insurance, etc.
    """
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Deduction'
        verbose_name_plural = 'Deductions'

    def __str__(self):
        return f'{self.name} - {self.amount}'

class Payslip(models.Model):
    """
    Represents a detailed payslip for each payroll payment to a trainer, including
    gross pay, deductions, and net pay.
    """
    payroll = models.OneToOneField(Payroll, on_delete=models.CASCADE)
    deductions = models.ManyToManyField(Deductions, blank=True, related_name='payslip_deductions')
    allowances = models.ManyToManyField(Allowances, blank=True, related_name='payslip_allowances')
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    issue_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Payroll.PAYROLL_STATUS_CHOICES, default='pending')

    class Meta:
        verbose_name = 'Payslip'
        verbose_name_plural = 'Payslips'

    def __str__(self):
        return f'Payslip for {self.payroll.trainer.user.username} on {self.issue_date}'

    def calculate_net_salary(self):
        """
        Calculate the net salary after applying deductions to the gross salary.
        """
        self.net_salary = self.gross_salary - self.deductions
        self.save()


# ======================== School Account Model ========================

class SchoolAccount(models.Model):
    """
    Represents the school's central account where all payments from students
    are collected and from which trainers are paid.

    - Ideally, we could have this information from an API or external system.
    """
    bank_name = models.CharField(max_length=100, default='')
    account_number = models.CharField(max_length=20, unique=True, default='')
    branch_code = models.CharField(max_length=10, default='')
    branch = models.CharField(max_length=100, default='')
    total_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'School Account'
        verbose_name_plural = 'School Accounts'

    def __str__(self):
        return f'{self.bank_name} Balance: {self.total_balance}'

    def add_funds(self, amount):
        """Add funds to the school account when students pay for courses."""
        self.total_balance += amount
        self.save()

    def deduct_funds(self, amount):
        """Deduct funds when trainers are paid."""
        if amount <= self.total_balance:
            self.total_balance -= amount
            self.save()
        else:
            raise ValueError("Insufficient funds in the school account.")

class Report(models.Model):
    """
    This model will store reports generated by managers or trainers.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(Manager, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        return self.title