# Generated by Django 4.1.6 on 2023-03-18 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0016_offername'),
    ]

    operations = [
        migrations.AddField(
            model_name='offername',
            name='productsname',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ss.productsname'),
            preserve_default=False,
        ),
    ]