from django.urls import path
from users.views import authorization_view, registration_view
urlpatterns = [
    path('authorization/', authorization_view),
    path('registration/', registration_view),
]