# Generated by Django 4.0.2 on 2022-02-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_property_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='CustomerProfile',
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Property Name'),
        ),
    ]
