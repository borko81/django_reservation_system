# Generated by Django 4.1.4 on 2022-12-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_roomtypemodel_name_short_alter_roomtypemodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]