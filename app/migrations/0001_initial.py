# Generated by Django 4.0.2 on 2022-02-15 18:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AI_Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('seeder_injection_date', models.DateField(default=django.utils.timezone.now)),
                ('injection_pgndn_date', models.DateField(default=django.utils.timezone.now)),
                ('gnrh_date', models.DateField(default=django.utils.timezone.now)),
                ('pull_seed_out_date', models.DateField(default=django.utils.timezone.now)),
                ('insemination_date', models.DateField(default=django.utils.timezone.now)),
                ('pregnancy_test_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='PIC (Property Identofication Code)')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('property_address', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('property_state', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('property_postcode', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('billing_address', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('billing_state', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('billing_postcode', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('abn', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('ai_program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ai_program')),
                ('pic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.property')),
            ],
        ),
    ]
