# Generated by Django 3.2.5 on 2021-09-05 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]