from django.contrib import admin
from billing.forms import DepositForm
from billing.models import Deposit
from billing.models import Call
from billing.models import User
from billing.user_admin import NamedUserAdmin


class DepositAdmin(admin.ModelAdmin):
    form = DepositForm

admin.site.register(User, NamedUserAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(Call)