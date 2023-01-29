from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    organization = models.CharField(max_length=256, default='')
    url = models.URLField(default='')
    mobile = models.CharField(max_length=32, default='')
    vcard = models.CharField(max_length=512, default='')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(receiver=create_profile, sender=User)
