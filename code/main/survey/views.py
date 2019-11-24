from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from survey.models import Survey
from survey.forms  import SurveyForm, AdvancedSurveyForm
class SurveyCreate(CreateView):
    model=Survey
    form_class=SurveyForm

class AdvancedSurveyCreate(CreateView):
    model=Survey
    form_class=AdvancedSurveyForm
