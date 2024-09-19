from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed users'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding the database with users...'))

        users = [
            {'username': 'admin-01', 'email': 'admin01@blog.com', 'password': '12345678', 'is_superuser': True},
            {'username': 'admin-02', 'email': 'admin02@blog.com', 'password': '12345678', 'is_superuser': True},
            {'username': 'user-01', 'email': 'user01@blog.com', 'password': '12345678', 'is_superuser': False},
            {'username': 'user-02', 'email': 'user02@blog.com', 'password': '12345678', 'is_superuser': False},
            {'username': 'user-03', 'email': 'user03@blog.com', 'password': '12345678', 'is_superuser': False},
            {'username': 'user-04', 'email': 'user04@blog.com', 'password': '12345678', 'is_superuser': False},
        ]

        for user_data in users:
            if User.objects.filter(email=user_data['email']).exists():
                self.stdout.write(self.style.WARNING(f"User with email {user_data['email']} already exists."))
            else:
                if user_data['is_superuser']:
                    User.objects.create_superuser(user_data['username'], user_data['email'], user_data['password'])
                else:
                    User.objects.create_user(user_data['username'], user_data['email'], user_data['password'])
                self.stdout.write(self.style.SUCCESS(f"Created user {user_data['username']}."))

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with users.'))
