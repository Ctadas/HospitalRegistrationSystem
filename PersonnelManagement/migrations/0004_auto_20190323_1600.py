# Generated by Django 2.1.7 on 2019-03-23 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PersonnelManagement', '0003_auto_20190323_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorinformation',
            old_name='gender',
            new_name='job_title',
        ),
    ]
