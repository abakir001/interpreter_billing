from django import forms
from django.contrib import admin
from billing.models import Deposit


class DepositForm(forms.ModelForm):

    class Meta:
        model = Deposit
        exclude = ['seconds', 'created_at']