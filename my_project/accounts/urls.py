# accounts/urls.py
from django.urls import path

from accounts import views
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]