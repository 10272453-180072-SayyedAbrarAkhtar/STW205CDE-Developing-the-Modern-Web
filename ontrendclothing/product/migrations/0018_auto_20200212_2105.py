# Generated by Django 3.0.1 on 2020-02-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20200212_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customize',
            name='mainbanner',
            field=models.ImageField(default='images/70550984_10157373051965535_3336865258831609856_n.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='customize',
            name='menbanner',
            field=models.ImageField(default='images/64514024_2171307086325281_2513036548014866432_n.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='customize',
            name='womenbanner',
            field=models.ImageField(default='images/66695107_2171307216325268_6767799174848053248_n.jpg', upload_to='images/'),
        ),
    ]
