from django import forms

# เพิ่มจากนี้
from django.utils.translation import gettext_lazy as _
from survey.models import Survey

from bootstrap_datepicker_plus import DatePickerInput
from crispy_forms.bootstrap import InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Reset, Row, Column

class SurveyForm(forms.ModelForm):
    class Meta:
        model=Survey
        fields="__all__"        
        widgets={
            'birthdate':DatePickerInput(format='%Y-%m-%d'),
            'gender': forms.RadioSelect(),
            'fruit': forms.RadioSelect(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()  
        self.helper.form_method = 'post' 
        self.helper.add_input(Submit('submit','Submit'))        
        self.helper.add_input(Submit('reset','Reset',css_class="btn btn-outline-primary"))        
        
class AdvancedSurveyForm(forms.ModelForm):
    class Meta:
        model=Survey
        fields="__all__"
        labels={
                'fullname': 'ชื่อ',
                'gender':'เพศ',
                'birthdate':'วันเดือนปีเกิด',
                'fruit':'ผลไม้ที่ท่านชอบ',
                'comment':'ข้อเสนอแนะ',
            }
        widgets={
                'birthdate':DatePickerInput(format='%Y-%m-%d'),
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()  
        self.helper.form_method = 'post'      
        self.helper.layout = Layout(
            Row(
                Column('fullname' ,css_class="form-group col-4"),                
                Column('email'    ,css_class="form-group col-4"),
                Column('birthdate',css_class="form-group col-4"),
                css_class='form-row',
            ),
            Row(
                Column(InlineRadios('gender'),css_class="form-group col-4"),
                Column(InlineRadios('fruit'),css_class="form-group col-4"),
            ),
            'comment',
            Submit('submit','ส่งแบบสำรวจ'),
            Reset('reset','ล้างข้อมูล'),
        )
        