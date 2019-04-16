# Generated by Django 2.1.7 on 2019-04-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalBusiness', '0007_auto_20190415_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorvisitsnumber',
            old_name='visits_time',
            new_name='visit_time',
        ),
        migrations.AlterField(
            model_name='doctorvisitsnumber',
            name='visit_number',
            field=models.IntegerField(default=30, verbose_name='剩余就诊次数'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='time',
            field=models.DateField(unique=True, verbose_name='值班时间'),
        ),
    ]