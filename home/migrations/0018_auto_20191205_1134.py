# Generated by Django 2.2.7 on 2019-12-05 11:34

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20191204_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='coming_soon',
            field=models.TextField(default='Coming Soon'),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='coming_soon_title',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
