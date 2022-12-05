from django import forms
class Myform(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    home = forms.IntegerField()
    fload = forms.IntegerField()
    
