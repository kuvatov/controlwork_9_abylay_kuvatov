from django.contrib.auth import get_user_model
from django.db import models


class Favourite(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favourites'
    )
    photo = models.ForeignKey(
        to='webapp.Photo',
        on_delete=models.CASCADE,
        verbose_name='Фотография',
        related_name='favourite'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )

    def __str__(self):
        return f'{self.user} - {self.photo}'
