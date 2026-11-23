from django.db import connection


class DatabaseRoleMiddleware:
    """Inject request identity and role into PostgreSQL session settings."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if connection.vendor == "postgresql":
            user = getattr(request, "user", None)
            role = "dispatcher" if getattr(user, "is_staff", False) else "reporter"
            user_id = str(getattr(user, "pk", "") or "")
            with connection.cursor() as cursor:
                cursor.execute("SELECT set_config('app.current_role', %s, true)", [role])
                cursor.execute("SELECT set_config('app.current_user_id', %s, true)", [user_id])

        return self.get_response(request)
