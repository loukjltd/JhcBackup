from django import forms


class OrderForm(forms.Form):
    dishName = forms.CharField(max_length=30)
    choices1 = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"))
    number = forms.ChoiceField(choices=choices1)


class UserForm(forms.Form):
    userName = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)