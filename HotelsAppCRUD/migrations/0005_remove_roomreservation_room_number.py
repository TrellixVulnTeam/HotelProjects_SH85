# Generated by Django 2.2.6 on 2019-11-18 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelsAppCRUD', '0004_auto_20191026_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomreservation',
            name='room_number',
        ),
    ]
