# Generated by Django 3.1.7 on 2021-02-24 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0002_auto_20210223_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='sales_app.product'),
        ),
    ]