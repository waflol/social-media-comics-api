import os

from django.core.files.storage import default_storage
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from user.models import User


@receiver(post_save, sender=User)
def add_default_image(sender, instance, created, **kwargs):
    if (
        created and not instance.avatar and not instance.cover
    ):  # Skip if instance is being created
        instance.avatar = "default/avatar_default.jpg"
        instance.cover = "default/cover_default.png"
        instance.save()
