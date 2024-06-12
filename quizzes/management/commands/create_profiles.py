from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from quizzes.models import UserProfile

class Command(BaseCommand):
    help = 'Create missing user profiles'

    def handle(self, *args, **kwargs):
        users = User.objects.filter(userprofile__isnull=True)
        for user in users:
            UserProfile.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Created profile for user {user.username}'))
