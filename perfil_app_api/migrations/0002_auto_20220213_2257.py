# Generated by Django 3.0.8 on 2022-02-14 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil_app_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='personas_table',
        ),
    ]