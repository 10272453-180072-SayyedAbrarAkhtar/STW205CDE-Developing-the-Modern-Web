# Generated by Django 3.0.1 on 2020-02-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20200212_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='customize',
            name='featureprodtitle',
            field=models.CharField(default='Ontrend this summer', max_length=50),
        ),
        migrations.AddField(
            model_name='customize',
            name='herosubtitle',
            field=models.CharField(default='Shop online', max_length=50),
        ),
        migrations.AddField(
            model_name='customize',
            name='herotitle',
            field=models.CharField(default='Stay home and', max_length=50),
        ),
    ]
