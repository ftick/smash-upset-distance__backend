# Generated by Django 3.1.2 on 2020-12-10 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upsets', '0007_auto_20201210_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='batch_update',
        ),
    ]
