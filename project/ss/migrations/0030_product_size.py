# Generated by Django 4.1.6 on 2023-03-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0029_remove_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
