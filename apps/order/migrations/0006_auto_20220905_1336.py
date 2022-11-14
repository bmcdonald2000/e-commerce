# Generated by Django 3.2.7 on 2022-09-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_used_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_shipped',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'ordered'), ('shipped', 'shipped'), ('arrived', 'arrived')], default='ordered', max_length=20),
        ),
    ]
