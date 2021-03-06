# Generated by Django 4.0.2 on 2022-02-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_customerprofile_ai_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerprofile',
            name='program_finished',
        ),
        migrations.AddField(
            model_name='ai_program',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='billing_state',
            field=models.CharField(blank=True, choices=[('TAS', 'TAS'), ('NSW', 'NSW'), ('VIC', 'VIC'), ('QLD', 'QLD'), ('NT', 'NT'), ('SA', 'SA'), ('WA', 'WA')], default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='property_state',
            field=models.CharField(blank=True, choices=[('TAS', 'TAS'), ('NSW', 'NSW'), ('VIC', 'VIC'), ('QLD', 'QLD'), ('NT', 'NT'), ('SA', 'SA'), ('WA', 'WA')], default='', max_length=100, null=True),
        ),
    ]
