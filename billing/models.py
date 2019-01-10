from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    name = models.CharField(verbose_name='name', max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['phone']


class Deposit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(verbose_name='Anount deposited', max_digits=10, decimal_places=2)
    seconds = models.IntegerField(verbose_name='Seconds deposited', blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='deposit'
    )

    def __str__(self):
        return '{} deposit. Amount: {}'.format(self.user, self.amount)


class Call(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(verbose_name='Call duration')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='call'
    )

    def __str__(self):
        return '{} call duration {}'.format(self.user, self.duration)
