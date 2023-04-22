from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='photos',
        verbose_name='Фотография'
    )
    signature = models.CharField(
        max_length=250,
        verbose_name='Подпись'
    )
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='photos'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )
    is_deleted = models.BooleanField(
        verbose_name="Удален",
        null=False,
        default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name="Дата и время удаления",
        null=True,
        default=None
    )

    def __str__(self):
        return self.signature

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()
