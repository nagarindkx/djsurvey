from django import forms

from survey.models import Survey
from crispy_forms.bootstrap import InlineRadios
from bootstrap_datepicker_plus import DatePickerInput
from django.utils.translation import gettext_lazy as _

class SurveyForm(forms.ModelForm):    
    class Meta:
        model=Survey
        fields="__all__"
        labels={
            'fullname': 'ชื่อ นามสกุล',
            'gender':'เพศ',
            'birthdate':'วันเดือนปีเกิด',
            'fruit':'ผลไม้ที่ท่านชอบ',
            'comment':'ข้อเสนอแนะ',
        }
        widgets={
            'birthdate':DatePickerInput(format='%Y-%m-%d'),
        }