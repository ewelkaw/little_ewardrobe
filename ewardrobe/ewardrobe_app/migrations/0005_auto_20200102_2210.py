# Generated by Django 3.0.1 on 2020-01-02 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewardrobe_app', '0004_auto_20200102_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='retailer',
            field=models.CharField(max_length=50),
        ),
    ]
