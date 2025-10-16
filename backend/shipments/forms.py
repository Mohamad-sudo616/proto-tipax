from django import forms
from .models import Package
from django.utils import timezone

CITY_CHOICES = [
    ('تهران', 'تهران'),
    ('اصفهان', 'اصفهان'),
    ('شیراز', 'شیراز'),
    ('تبریز', 'تبریز'),
    ('مشهد', 'مشهد'),
    ('رشت', 'رشت'),
    ('اهواز', 'اهواز'),
    ('کرج', 'کرج'),
]

SHIP_TYPE_CHOICES = [
    ('درون‌شهری', 'درون‌شهری'),
    ('بین‌شهری', 'بین‌شهری'),
]

class PackageForm(forms.ModelForm):
    ship_type = forms.ChoiceField(
        choices=SHIP_TYPE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label='نوع ارسال'
    )

    from_location = forms.ChoiceField(
        choices=CITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='شهر مبدا'
    )

    to_location = forms.ChoiceField(
        choices=CITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='شهر مقصد'
    )

    send_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        initial=timezone.now().date(),
        label='تاریخ ارسال'
    )

    class Meta:
        model = Package
        fields = [
            'ship_type',
            'from_location', 'to_location',
            'from_address', 'to_address',
            'weight_kg', 'notes', 'send_date'
        ]
        labels = {
            'from_address': 'آدرس مبدا',
            'to_address': 'آدرس مقصد',
            'weight_kg': 'وزن (کیلوگرم)',
            'notes': 'توضیحات',
        }
        widgets = {
            'from_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'to_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'weight_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
