# Generated by Django 3.1.2 on 2020-11-07 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20201106_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='type',
            field=models.CharField(default='', max_length=50),
        ),
    ]
