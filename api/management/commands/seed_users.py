from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Seed users'

    def handle(self, *args, **options):
        User.objects.create_superuser('admin-01', 'admin01@blog.com', '12345678')
        User.objects.create_superuser('admin-02', 'admin02@blog.com', '12345678')
        User.objects.create_user('user-01', 'user01@blog.com', '12345678')
        User.objects.create_user('user-02', 'user02@blog.com', '12345678')
        User.objects.create_user('user-03', 'user03@blog.com', '12345678')
        User.objects.create_user('user-04', 'user04@blog.com', '12345678')
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with users.'))
