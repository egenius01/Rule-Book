# Generated by Django 2.2.7 on 2020-01-03 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0006_masterrulebook_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterrulebook',
            name='initial_date_of_rendition',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
