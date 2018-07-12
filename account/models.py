from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField('出生日期', blank=True, null=True)
    photo = models.ImageField('照片', upload_to='users/%Y/%m/%d', blank=True)
    def __str__(self):
        return '{}的个人资料'.format(self.user.username)