from django.urls import path

from silantaccountsapp.views import (silant_login, silant_logout)

urlpatterns = [
    path("login/", silant_login, name="silant_login"),
    path("logout/", silant_logout, name="silant_logout"),
]
