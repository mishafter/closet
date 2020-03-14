from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Crate a superuser, and allow password to be provided'

    def handle(self, *args, **options):
        if User.objects.filter(username = 'admin').exists():
            return

        User.objects.create_superuser('admin', 'admin@example.com', 'admin')