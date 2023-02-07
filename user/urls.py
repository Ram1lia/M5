from django.urls import path
from users.views import *

urlpatterns = [
    path('authorization/', AuthorizationCreateAPIView.as_view()),
    path('registration/', RegistrationCreateAPIView.as_view()),
]