# Generated by Django 4.0.2 on 2022-02-19 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_alter_cowtable_breed_alter_cowtable_condition_score_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ai_program',
            old_name='gnrh_date',
            new_name='bomerol_date',
        ),
        migrations.RenameField(
            model_name='ai_program',
            old_name='gnrh_status',
            new_name='bomerol_status',
        ),
    ]