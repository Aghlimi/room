from django import forms
from .models import *


class Post(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["text", "image"]
        widget = {"text": forms.TextInput(attrs={"placeholder": "post text"})}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False
        self.fields["image"].required = False


class Comment(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["text", "image"]
        widget = {"text": forms.TextInput(attrs={"placeholder": "comment text"})}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False
        self.fields["image"].required = False


class React(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["text", "image"]
        widget = {"text": forms.TextInput(attrs={"placeholder": "comment text"})}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False
        self.fields["image"].required = False
