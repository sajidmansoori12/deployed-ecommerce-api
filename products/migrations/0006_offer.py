# Generated by Django 3.1.2 on 2020-10-31 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201030_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_name', models.CharField(default='Null', max_length=50)),
                ('offer_image', models.ImageField(upload_to='offer/')),
            ],
        ),
    ]
