# Generated by Django 5.1.4 on 2024-12-12 03:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Product')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Price')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Discount in %')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.categories', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
    ]
