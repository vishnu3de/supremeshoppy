# Generated by Django 4.1.6 on 2023-03-22 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0047_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ss.product'),
            preserve_default=False,
        ),
    ]