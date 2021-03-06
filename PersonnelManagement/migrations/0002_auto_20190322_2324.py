# Generated by Django 2.1.7 on 2019-03-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonnelManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinformation',
            name='gender',
            field=models.CharField(choices=[('chief_physician', '主任医师'), ('deputy_chief_physician', '副主任医师'), ('attending_physician', '主治医师'), ('physician', '医师')], max_length=30, verbose_name='医生职称'),
        ),
    ]
