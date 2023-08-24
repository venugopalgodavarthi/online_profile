from django import forms
from userprofile.models import UserProfile_model


class UserProfile_form(forms.ModelForm):
    class Meta:
        model = UserProfile_model
        fields = "__all__"
