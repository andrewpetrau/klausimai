# Generated by Django 4.2.5 on 2023-09-09 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Klausimas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tekstas', models.TextField()),
                ('atsakymas', models.TextField(blank=True, null=True)),
                ('atsake_vartotojas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atsakymai', to=settings.AUTH_USER_MODEL)),
                ('uzduotas_vartotojas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='klausimai', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
