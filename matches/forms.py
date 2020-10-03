from django import forms
from .models import Match

class MatchModelForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['op_name', 'op_email', 'op_number', 'pub_date', 'money_needed', 'money_spending', 'store', 'resolved']