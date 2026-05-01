from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL("SET FOREIGN_KEY_CHECKS=0;"),
        migrations.RunSQL("DROP TABLE IF EXISTS usuarios_user_groups;"),
        migrations.RunSQL("DROP TABLE IF EXISTS usuarios_user_user_permissions;"),
        migrations.RunSQL("DROP TABLE IF EXISTS usuarios_user;"),
        migrations.RunSQL("SET FOREIGN_KEY_CHECKS=1;"),
    ]
