# Generated by Django 4.1.7 on 2023-03-18 12:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_alter_story_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
