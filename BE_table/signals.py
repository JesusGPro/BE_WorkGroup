from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FollowupBE

# Define a custom signal
user_created = receiver(post_save, sender=FollowupBE)