from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class BalanceForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the amount to add to your balance.")

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
