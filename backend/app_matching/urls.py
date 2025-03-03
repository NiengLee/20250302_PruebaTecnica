from django.urls import path, include
from .views import FindBestMatch

urlpatterns = [
    path('find-best-match/', FindBestMatch.as_view(), name="find-best-match"),
]