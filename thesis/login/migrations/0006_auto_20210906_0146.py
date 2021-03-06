# Generated by Django 3.2.5 on 2021-09-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210821_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thesis',
            old_name='assigned',
            new_name='ExaminorId',
        ),
        migrations.RenameField(
            model_name='thesis',
            old_name='field',
            new_name='Speciality',
        ),
        migrations.RenameField(
            model_name='thesis',
            old_name='name',
            new_name='Student_Name',
        ),
        migrations.RenameField(
            model_name='thesis',
            old_name='Id',
            new_name='TitleId',
        ),
        migrations.RemoveField(
            model_name='thesis',
            name='feedack',
        ),
        migrations.AddField(
            model_name='thesis',
            name='Remarks',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thesis',
            name='Status',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='thesis',
            name='Thesis_Type',
            field=models.BooleanField(default=0),
        ),
    ]
