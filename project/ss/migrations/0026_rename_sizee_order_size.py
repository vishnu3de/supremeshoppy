# Generated by Django 4.1.6 on 2023-03-20 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0025_rename_size_order_sizee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='sizee',
            new_name='size',
        ),
    ]
