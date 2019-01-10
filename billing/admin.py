from django.contrib import admin
from billing.forms import DepositForm
from billing.models import Deposit
from billing.models import Call


class DepositAdmin(admin.ModelAdmin):
    form = DepositForm

admin.site.register(Deposit, DepositAdmin)
admin.site.register(Call)