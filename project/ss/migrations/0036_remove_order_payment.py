# Generated by Django 4.1.6 on 2023-03-20 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0035_remove_order_phone_remove_order_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
    ]
