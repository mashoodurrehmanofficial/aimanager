# Generated by Django 4.0.2 on 2022-02-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_profile_mobile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='PIC (Property Identofication Code)'),
        ),
    ]