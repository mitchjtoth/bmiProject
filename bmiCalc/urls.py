from django.urls import path
from bmiCalc import views

urlpatterns = [
    path("", views.calculate_bmi, name="calculate_bmi"),
]