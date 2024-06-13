from django import forms
from . import models

class CreateOTP(forms.ModelForm):
    class Meta:
        model = models.OTP
        fields = ('username', 'otp_code', 'created_at', 'email')

