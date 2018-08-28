from django import forms

class GetSomeForm(forms.Form):
    amount = forms.FloatField(label ="Количество USD",min_value=0)
