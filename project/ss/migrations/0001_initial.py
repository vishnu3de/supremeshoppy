# Generated by Django 4.1.5 on 2023-02-17 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShiAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housename', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housename', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images')),
                ('image1', models.ImageField(upload_to='static/images')),
                ('image2', models.ImageField(upload_to='static/images')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=400)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ss.category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='productsname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ss.productsname'),
        ),
    ]
