# Generated by Django 5.0.4 on 2024-05-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_remove_task_employee_task_customer_delete_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.TextField(blank=True, null=True),
        ),
    ]
