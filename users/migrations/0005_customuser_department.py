# Generated by Django 2.2.7 on 2019-12-30 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Department'),
        ),
    ]