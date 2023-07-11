from django.urls import path
from .views import user_input_view, input_success

urlpatterns = [
    path('input/', user_input_view, name='user_input'),
    path('input/success/', input_success, name='input_success'),
]
