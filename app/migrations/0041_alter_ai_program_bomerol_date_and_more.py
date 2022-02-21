# Generated by Django 4.0.2 on 2022-02-21 02:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_rename_bomerol_injection_date_ai_program_pg_injection_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ai_program',
            name='bomerol_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Bomerol'),
        ),
        migrations.AlterField(
            model_name='ai_program',
            name='cidrs_in_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='CIDRS In'),
        ),
        migrations.AlterField(
            model_name='ai_program',
            name='cidrs_out_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='CIDRS Out'),
        ),
        migrations.AlterField(
            model_name='ai_program',
            name='insemination_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Insemination'),
        ),
        migrations.AlterField(
            model_name='ai_program',
            name='last_completed_action',
            field=models.CharField(blank=True, default='N/A', max_length=50, null=True, verbose_name='Last completed action'),
        ),
        migrations.AlterField(
            model_name='ai_program',
            name='pg_injection_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='PG Injection'),
        ),
        migrations.AlterField(
            model_name='ai_program',
            name='pregnancy_test_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Pregnancy Test'),
        ),
        migrations.AlterField(
            model_name='ai_program',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=''),
        ),
    ]
