from django.http import JsonResponse
from django.urls import path

from backend.transactions.views import incident_list_create


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("api/health/", health),
    path("api/incidents/", incident_list_create),
]
