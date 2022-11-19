# Generated by Django 4.1.2 on 2022-10-25 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name of clothes')),
            ],
        ),
        migrations.CreateModel(
            name='Gender_clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Gender of clothes')),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_name', models.CharField(max_length=50, verbose_name='Name of clothes')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Image')),
                ('size', models.IntegerField(verbose_name='Size of clothes')),
                ('color', models.CharField(max_length=70, verbose_name='Color of clothes')),
                ('publication', models.BooleanField(default=True, verbose_name='Publication')),
                ('sent_at', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('brand_of_clothes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop_app.brand', verbose_name='Brand of clothes')),
                ('gender_of_clothes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop_app.gender_clothes', verbose_name='Gender of clothes')),
            ],
        ),
    ]
