from django import forms

class NameForm(forms.Form):
    cityname = forms.CharField(label='cityname', max_length=20)
