# Generated by Django 3.0.1 on 2020-01-02 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewardrobe_app', '0006_auto_20200102_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]
