from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise ValueError('Users must have a phone number')

        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class AbstractPhoneUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(_('phone number'), max_length=255, unique=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True
        ordering = ['phone']
    
    def get_full_name(self):
        return self.phone

    def get_short_name(self):
        return self.phone


@python_2_unicode_compatible
class AbstractNamedUser(AbstractPhoneUser):
    name = models.CharField(_('name'), max_length=255, blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['phone', 'name']

    def __str__(self):
        return '{phone} {name}'.format(
            name=self.name,
            phone=self.phone,
        )

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name