from django.test import TestCase


class IncidentApiTests(TestCase):
    def test_health_endpoint(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_create_incident(self):
        response = self.client.post(
            "/api/incidents/",
            data={
                "description": "House fire",
                "latitude": 13.941,
                "longitude": 121.163,
                "severity": "high",
                "reporter_id": "phone-123",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["description"], "House fire")

    def test_reject_invalid_incident(self):
        response = self.client.post(
            "/api/incidents/",
            data={"description": "Missing coordinates"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
