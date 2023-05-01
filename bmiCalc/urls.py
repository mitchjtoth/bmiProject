from django.urls import path
from bmiCalc import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.calculate_bmi, name="calculate_bmi"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)