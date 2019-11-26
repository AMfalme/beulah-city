# Generated by Django 2.2.7 on 2019-11-25 15:38

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0009_auto_20191125_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', models.CharField(blank=True, max_length=250)),
                ('intro', models.CharField(blank=True, max_length=250)),
                ('hero_intro', wagtail.core.fields.RichTextField(blank=True)),
                ('about_title', models.TextField(default='Who we are')),
                ('about_paragraph', models.TextField(blank=True)),
                ('projects_overview_title', models.TextField(blank=True)),
                ('projects_overview', models.TextField(blank=True)),
                ('company_overview', models.TextField(blank=True)),
                ('company_overview_paragraph', models.TextField(blank=True)),
                ('company_pride', models.TextField(blank=True)),
                ('company_pride_paragraph', models.TextField(blank=True)),
                ('company_overview_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('company_pride_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='OverviewImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('overview_name', models.TextField(default='P')),
                ('overview_info', models.TextField(blank=True)),
                ('overview_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='overview_images', to='home.AboutPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
