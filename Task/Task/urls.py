from django.contrib import admin
from django.urls import path,include
from home.views import user_input_view, input_success


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', user_input_view, name='user_input'),
    path('input/success/', input_success, name='input_success'),
]
