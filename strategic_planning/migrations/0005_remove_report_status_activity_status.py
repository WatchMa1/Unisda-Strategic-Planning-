# Generated by Django 5.0.6 on 2024-11-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategic_planning', '0004_alter_report_goal_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='status',
        ),
        migrations.AddField(
            model_name='activity',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]