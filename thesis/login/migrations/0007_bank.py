# Generated by Django 3.2.5 on 2021-09-05 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0006_auto_20210906_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IFSC', models.CharField(max_length=20)),
                ('Name_place', models.CharField(max_length=100)),
                ('account_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('ExaminorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
