# Generated by Django 3.2.7 on 2022-08-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
