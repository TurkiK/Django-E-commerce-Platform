from django import forms

class BalanceForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the amount to add to your balance.")
