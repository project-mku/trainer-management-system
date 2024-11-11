import random
import string
from django.core.management.base import BaseCommand
from core.models import CustomUser, Trainer
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Create users and trainers'

    def generate_random_string(self, length=8):
        """Generate a random string of fixed length."""
        letters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters) for i in range(length))
    
    def get_department(self):
        """Return a random department."""
        departments = ['HR', 'IT', 'Finance', 'Sales', 'Marketing', 'Operations', 'Customer Service']
        return random.choice(departments)
    
    def get_years_of_experience(self):
        """Return a random number between 1 and 7."""
        return random.randint(1, 7)
    
    def get_base_salary(self):
        """Return a random number between 50000 and 200000."""
        return random.randint(50000, 200000)
    
    def get_payroll_status(self):
        """Return a random payroll status."""
        return random.choice([True, False])
    
    def get_id_number(self):
        """Return a random ID number."""
        return random.randint(10000000, 99999999)

    def handle(self, *args, **kwargs):
        try:
            users_to_create = []
            trainers_to_create = []

            # Create users and trainers
            for i in range(1, 51):
                email = f'trainer{i}_{self.generate_random_string()}@gmail.com'

                # Create and save each user individually to ensure password is hashed
                user = CustomUser(
                    username=email,
                    email=email,
                    gender='male',
                    is_trainer=True,
                )
                user.set_password('password')  # Set and hash the password
                user.save()
                
                # Prepare trainer instance linked to this user
                trainer = Trainer(
                    user=user,
                    first_name=f'Trainer {i}',
                    last_name=f'Lastname {i}',
                    phone_number='0712345678',
                    department=self.get_department(),
                    years_of_experience=self.get_years_of_experience(),
                    base_salary=self.get_base_salary(),
                    on_payroll=self.get_payroll_status(),
                    email=user.email,
                    id_number=self.get_id_number(),
                    bio='I am a trainer',
                )
                trainers_to_create.append(trainer)

            # Bulk create trainers after all users are created
            Trainer.objects.bulk_create(trainers_to_create)
            self.stdout.write(self.style.SUCCESS(f"Successfully created {len(trainers_to_create)} trainers."))

        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f"IntegrityError occurred: {e}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
