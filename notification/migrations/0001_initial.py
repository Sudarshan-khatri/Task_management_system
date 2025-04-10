# Generated by Django 5.2 on 2025-04-09 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
        ('TaskMode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=25555)),
                ('notification_type', models.CharField(choices=[('ASSIGNMENT', 'Assignment'), ('DEADLINE', 'Deadline'), ('COMMENT', 'Comment'), ('STATUS_CHANGE', 'Status_change')], default='Comment', max_length=255)),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('related_task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TaskMode.taskaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.usermodel')),
            ],
        ),
    ]
