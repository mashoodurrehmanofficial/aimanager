# Generated by Django 4.0.2 on 2022-02-20 04:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_cowtable_nlsid_alter_customerprofile_abn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='abn',
            field=models.CharField(default='', max_length=20, validators=[django.core.validators.RegexValidator('^\\d[0-9]\\s\\d[0-9].\\s\\d[0-9].\\s\\d[0-9].')]),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='billing_postcode',
            field=models.CharField(blank=True, default='', max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')]),
        ),
        migrations.AlterField(
            model_name='property',
            name='pic',
            field=models.CharField(blank=True, default='', max_length=8, null=True, verbose_name='PIC (Property Identofication Code)'),
        ),
    ]
