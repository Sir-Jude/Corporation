from django.urls import path
from . import views

app_name = "corporation"
urlpatterns = [
    path("new/", views.NewCorporationView.as_view(), name="new"),
    path("<int:pk>/", views.CorporationDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditCorporationView.as_view(), name="edit"),
]
