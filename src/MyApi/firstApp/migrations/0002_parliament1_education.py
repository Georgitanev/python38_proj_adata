# Generated by Django 3.2.2 on 2021-05-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="parliament1",
            name="education",
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]