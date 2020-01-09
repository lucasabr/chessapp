# Generated by Django 3.0.2 on 2020-01-09 22:57

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_played', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=models.SET('DeletedUser'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
