from django.contrib import admin
from billing.models import Deposit
from billing.models import Call

admin.site.register(Deposit)
admin.site.register(Call)