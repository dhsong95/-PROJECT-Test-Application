from django.urls import path
from . import views

app_name = 'tests'

urlpatterns = [
    path('', views.TestListView.as_view(), name='test_list'),
]