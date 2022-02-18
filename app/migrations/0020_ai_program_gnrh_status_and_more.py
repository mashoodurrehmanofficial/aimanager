# Generated by Django 4.0.2 on 2022-02-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_cowtable_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='ai_program',
            name='gnrh_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='ai_program',
            name='injection_pgndn_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='ai_program',
            name='insemination_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='ai_program',
            name='pregnancy_test_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='ai_program',
            name='pull_seed_out_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='ai_program',
            name='seeder_injection_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]