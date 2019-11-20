from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from survey.models import Survey
from survey.forms  import SurveyForm
class SurveyCreate(CreateView):
    model=Survey
    form_class=SurveyForm
