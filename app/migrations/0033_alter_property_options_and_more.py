# Generated by Django 4.0.2 on 2022-02-19 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_rename_gnrh_date_ai_program_bomerol_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Properties'},
        ),
        migrations.RenameField(
            model_name='ai_program',
            old_name='seeder_injection_date',
            new_name='cidrs_in_date',
        ),
        migrations.RenameField(
            model_name='ai_program',
            old_name='seeder_injection_status',
            new_name='cidrs_in_status',
        ),
    ]
