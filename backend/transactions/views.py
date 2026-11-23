import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Incident


@require_http_methods(["GET", "POST"])
def incident_list_create(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body or "{}")
            incident = Incident.objects.create(
                description=str(payload["description"]),
                latitude=float(payload["latitude"]),
                longitude=float(payload["longitude"]),
                severity=str(payload.get("severity", "unknown")),
                reporter_id=str(payload.get("reporter_id", "")),
            )
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            return JsonResponse({"detail": "Invalid incident payload."}, status=400)

        return JsonResponse(
            {
                "id": incident.id,
                "description": incident.description,
                "latitude": incident.latitude,
                "longitude": incident.longitude,
                "severity": incident.severity,
                "reporter_id": incident.reporter_id,
                "created_at": incident.created_at.isoformat(),
            },
            status=201,
        )

    incidents = list(
        Incident.objects.values(
            "id", "description", "latitude", "longitude",
            "severity", "reporter_id", "created_at",
        )[:100]
    )
    return JsonResponse({"incidents": incidents})
