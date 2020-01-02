# Generated by Django 2.2.4 on 2020-01-02 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200101_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
