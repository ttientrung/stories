# Generated by Django 4.1.7 on 2023-03-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story_image_story_summary_story_viewed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
