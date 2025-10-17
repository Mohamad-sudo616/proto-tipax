# tracking/forms.py
from django import forms

class TrackingForm(forms.Form):
    tracking_code = forms.CharField(
        max_length=64,
        label='Tracking Code',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your tracking code',
            'class': 'form-control'
        })
    )

    def clean_tracking_code(self):
        code = self.cleaned_data['tracking_code'].strip()
        import re
        if not re.match(r'^[A-Za-z0-9-_]+$', code):
            raise forms.ValidationError('Invalid tracking code format.')
        return code
