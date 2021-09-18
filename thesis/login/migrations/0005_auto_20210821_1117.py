# Generated by Django 3.2.5 on 2021-08-21 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0004_alter_thesis_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='assigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Examinor',
        ),
    ]
