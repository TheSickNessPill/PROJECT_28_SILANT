from django.urls import path

from silantmashinesapp.views import (
    base_mashines, full_data_by_user
)

urlpatterns = [
    path("baseMasines/", base_mashines, name="base_mashines"),
    path("fullDataByUser/", full_data_by_user, name="full_data_by_user"),
]