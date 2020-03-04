from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Test
from .models import Question


# Create your views here.
class TestListView(ListView):
    model = Test
