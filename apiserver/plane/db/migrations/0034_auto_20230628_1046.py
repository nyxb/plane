# Generated by Django 3.2.19 on 2023-06-28 05:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0033_auto_20230618_2125"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timelineissue",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="timelineissue",
            name="issue",
        ),
        migrations.RemoveField(
            model_name="timelineissue",
            name="project",
        ),
        migrations.RemoveField(
            model_name="timelineissue",
            name="updated_by",
        ),
        migrations.RemoveField(
            model_name="timelineissue",
            name="workspace",
        ),
        migrations.DeleteModel(
            name="Shortcut",
        ),
        migrations.DeleteModel(
            name="TimelineIssue",
        ),
    ]
