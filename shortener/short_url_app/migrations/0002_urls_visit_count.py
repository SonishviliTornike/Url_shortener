# Generated by Django 5.0.4 on 2024-04-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_url_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='visit_count',
            field=models.IntegerField(default=0),
        ),
    ]
