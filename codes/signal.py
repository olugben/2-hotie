from user.models import CustomUser
from django.dispatch import receiver
from .models import  Codes
from django.db.models.signals import post_save


@receiver(post_save, sender=CustomUser)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
    if created:
        Codes.objects.create(user=instance)