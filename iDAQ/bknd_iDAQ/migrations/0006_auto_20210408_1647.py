# Generated by Django 2.0.2 on 2021-04-08 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bknd_iDAQ', '0005_auto_20210408_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mst_dev_addr',
            old_name='deviceName',
            new_name='devicesName',
        ),
    ]
