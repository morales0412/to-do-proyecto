from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("to_do_app", "0001_initial"),
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tarea",
            name="usuario",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="usuarios.user",
            ),
        ),
    ]
