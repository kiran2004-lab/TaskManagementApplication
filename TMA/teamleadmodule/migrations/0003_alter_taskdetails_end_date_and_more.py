# Generated by Django 5.0.2 on 2024-02-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamleadmodule', '0002_taskdetails_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdetails',
            name='End_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='taskdetails',
            name='Start_Date',
            field=models.DateField(),
        ),
    ]
