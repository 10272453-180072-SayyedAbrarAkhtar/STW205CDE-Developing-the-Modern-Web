# Generated by Django 3.0.1 on 2020-02-10 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200210_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='img',
            new_name='displayImg',
        ),
    ]
