from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Deposit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(verbose_name='Amount deposited', max_digits=10, decimal_places=2)
    seconds = models.IntegerField(verbose_name='Seconds deposited', blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='deposit'
    )

    def __str__(self):
        return '{} deposit Amount: {}, Seconds: {}, Date: {}'.format(
            self.user, self.amount, self.seconds, self.created_at)

    def save(self, *args, **kwargs):
        # self.amount is entered in Soms.
        # Currency is converted to USD ($1 == 70 Soms) and multiplied by 60
        # This is how we calculate seconds
        CURRENCY_RATE = 70
        SECONDS_IN_MINUTE = 60
        self.seconds = self.amount * SECONDS_IN_MINUTE / CURRENCY_RATE
        super().save(*args, **kwargs)


class Call(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(verbose_name='Call duration')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='call'

    )

    def __str__(self):
        return '{} call duration: {} date: {}'.format(self.user, self.duration, self.created_at)

