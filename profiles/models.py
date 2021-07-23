from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    bio= models.TextField(default='Include bio here....')
    avatar= models.ImageField(upload_to='avatars',default='no_picture.png')
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    def get_username(self):
        return str(self.user.username)

@receiver (post_save, sender=User)
def update_profile_signal(sender, instance , created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
