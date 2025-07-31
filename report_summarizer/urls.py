from django.urls import path
from .views import summarize_report_view

urlpatterns = [
    path('summarize/<int:report_id>/', summarize_report_view, name='summarize_report'),
]