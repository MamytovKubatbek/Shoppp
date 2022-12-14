# Generated by Django 4.1.2 on 2022-10-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name=' full_name')),
                ('email', models.CharField(max_length=1000, verbose_name='email')),
                ('password', models.IntegerField(verbose_name='password')),
                ('address', models.CharField(max_length=1000, verbose_name='address')),
                ('phone_number', models.TextField(verbose_name='phone_number')),
                ('sent_at', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
