from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_onboarding", "0004_create_onboardingdevice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onboardingtask", name="created", field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
