from django.db import migrations, models


def enable_incident_rls(apps, schema_editor):
    if schema_editor.connection.vendor != "postgresql":
        return
    table = schema_editor.quote_name("transactions_incident")
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("ALTER TABLE %s ENABLE ROW LEVEL SECURITY" % table)
        cursor.execute(
            "CREATE POLICY incident_dispatcher ON %s "
            "FOR ALL USING (current_setting('app.current_role', true) = 'dispatcher') "
            "WITH CHECK (current_setting('app.current_role', true) = 'dispatcher')" % table
        )
        cursor.execute(
            "CREATE POLICY incident_reporter ON %s "
            "FOR ALL USING (reporter_id = current_setting('app.current_user_id', true)) "
            "WITH CHECK (reporter_id = current_setting('app.current_user_id', true))" % table
        )


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Incident",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("description", models.CharField(max_length=255)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("severity", models.CharField(default="unknown", max_length=32)),
                ("reporter_id", models.CharField(blank=True, max_length=64)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.RunPython(enable_incident_rls, migrations.RunPython.noop),
    ]
