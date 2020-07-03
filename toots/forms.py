from django import forms
from django.conf import settings
from .models import Toot

MAX_LENGTH = settings.MAX_LENGTH

class TootForm(forms.ModelForm):
    class Meta:
        model = Toot
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_LENGTH:
            raise forms.ValidationError(
                "The toot is too long! The elephant is suffocating!"
            )

        if len(content) == 0:
            raise forms.ValidationError(
                "That is a silent toot!"
            )

        return content

