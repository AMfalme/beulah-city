# Generated by Django 2.2.7 on 2019-11-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191119_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='css_strings',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='project_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='project_title',
            field=models.TextField(default='Inclusionary space design'),
        ),
    ]
