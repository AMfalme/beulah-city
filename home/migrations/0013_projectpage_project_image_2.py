# Generated by Django 2.2.7 on 2019-11-27 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0012_projects_project_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='project_image_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]