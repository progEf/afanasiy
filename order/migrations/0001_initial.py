# Generated by Django 4.2.1 on 2023-06-06 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('afas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('el', models.CharField(choices=[('bottle', 'bottle '), ('packaging', 'packaging')], max_length=200)),
                ('stat_time', models.DateField(null=True)),
                ('end_time', models.DateField(null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='product_discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('el', models.CharField(choices=[('bottle', 'bottle '), ('packaging', 'packaging')], max_length=200)),
                ('stat_time', models.DateField(null=True)),
                ('end_time', models.DateField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('discount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Comp_Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_procent', models.IntegerField(null=True)),
                ('Comapany_Cl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afas.comapany_client_id')),
                ('Shops_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='afas.comapany_cl_id_and_shops')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='order_products_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('sumir', models.IntegerField(null=True)),
                ('stat_time', models.DateField(null=True)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.product_admin')),
                ('id_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.user_comp_shop')),
            ],
        ),
        migrations.CreateModel(
            name='order_Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order_products_user')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.user_comp_shop')),
            ],
        ),
    ]
