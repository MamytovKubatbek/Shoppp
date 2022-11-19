# Generated by Django 4.1.2 on 2022-10-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_order_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name_products',
            field=models.TextField(default=1, verbose_name='name_products'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=50, verbose_name='phone_number'),
        ),
    ]
