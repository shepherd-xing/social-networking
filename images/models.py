from django.db import models
from django.conf import settings
from django.utils.text import slugify
# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', related_name='images_created')
    title = models.CharField('标题', max_length=200)
    slug = models.CharField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField('图片', upload_to='images/%Y/%m/%d')
    description = models.TextField('描述', blank=True)
    created = models.DateField('创建日期', auto_now_add=True, db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='喜欢该图片的用户',
                                        related_name='images_liked', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)













