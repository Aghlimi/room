from django import forms


class Create(forms.Form):
    type = forms.ChoiceField(choices=[("group", "group"), ("two", "two")])
