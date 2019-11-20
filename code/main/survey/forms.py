from django import forms

from survey.models import Survey
from crispy_forms.bootstrap import InlineRadios
from bootstrap_datepicker_plus import DatePickerInput
from django.utils.translation import gettext_lazy as _

class SurveyForm(forms.ModelForm):    
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),
        label='เพศ',
        choices=[('F','หญิง'),('M','ชาย')],
    )
    fruit=forms.ChoiceField(
        widget=forms.RadioSelect(),
        label='ผลไม้ที่ท่านชอบ',
        choices=[('a','แอปเปิล'),('b','กล้วย'),('c','มะพร้าว'),('d','ทุเรียน')],
    )

    class Meta:
        model=Survey
        fields="__all__"
        widgets={
            'birthdate':DatePickerInput(format='%Y-%m-%d')
        }