# Generated by Django 4.1.6 on 2023-03-20 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0028_rename_sizee_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
