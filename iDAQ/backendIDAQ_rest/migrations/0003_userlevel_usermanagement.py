# Generated by Django 3.1.7 on 2021-03-22 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendIDAQ_rest', '0002_datatable_shifttable'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserLevelID', models.UUIDField()),
                ('LevelName', models.CharField(max_length=30)),
                ('LevelNamePriority', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.UUIDField()),
                ('Username', models.CharField(max_length=30)),
                ('PassWord', models.CharField(max_length=10)),
                ('UserLevelID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendIDAQ_rest.userlevel')),
            ],
        ),
    ]
