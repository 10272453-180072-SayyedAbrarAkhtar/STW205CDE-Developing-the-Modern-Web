# Generated by Django 3.0.1 on 2020-02-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200209_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('key', models.CharField(max_length=50)),
                ('img', models.ImageField(default='img.jpg', upload_to='images/')),
                ('prodreview', models.TextField()),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]
