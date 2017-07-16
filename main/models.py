import os
from django.conf import settings
from django.db import models
from django.dispatch import receiver


class Files(models.Model):
    name = models.CharField(max_length=50, verbose_name='文件名称')
    file = models.FileField(upload_to='files', verbose_name='上传')
    desc = models.CharField(max_length=120, verbose_name='概要')
    detail = models.TextField(default='', verbose_name='详细描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '资料维护'


@receiver(models.signals.post_save, sender=Files)
def save_filesize(sender, instance, *args, **kwargs): # instance是刚才保存的实例
    size = os.path.getsize(os.path.join(settings.MEDIA_ROOT, str(instance.file)))/1000

