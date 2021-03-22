# Generated by Django 3.1.7 on 2021-03-22 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendIDAQ_rest', '0004_plcaddress_unitid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datatable',
            name='id',
        ),
        migrations.RemoveField(
            model_name='plcaddress',
            name='id',
        ),
        migrations.RemoveField(
            model_name='plctcpconnection',
            name='id',
        ),
        migrations.RemoveField(
            model_name='shifttable',
            name='id',
        ),
        migrations.RemoveField(
            model_name='unittable',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userlevel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usermanagement',
            name='id',
        ),
        migrations.AlterField(
            model_name='datatable',
            name='DataID',
            field=models.Field(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plcaddress',
            name='plcDataAddrID',
            field=models.Field(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plcaddress',
            name='unitID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendIDAQ_rest.unittable'),
        ),
        migrations.AlterField(
            model_name='plctcpconnection',
            name='plcID',
            field=models.Field(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shifttable',
            name='ShiftID',
            field=models.Field(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unittable',
            name='unitID',
            field=models.Field(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='UserLevelID',
            field=models.Field(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usermanagement',
            name='UserID',
            field=models.Field(primary_key=True, serialize=False),
        ),
    ]
