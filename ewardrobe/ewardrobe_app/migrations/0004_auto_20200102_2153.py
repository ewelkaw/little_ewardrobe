# Generated by Django 3.0.1 on 2020-01-02 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ewardrobe_app', '0003_remove_product_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='reviews_count',
            new_name='review_count',
        ),
    ]
