# Generated by Django 3.0.1 on 2020-02-25 18:35

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('ewardrobe_app', '0018_auto_20200218_2127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'ordering': ['date_created'], 'verbose_name_plural': 'Baskets'},
        ),
        migrations.AlterField(
            model_name='basket',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(0, 'opened'), (1, 'paid'), (2, 'shipped'), (3, 'closed'), (4, 'returned')], default=0, protected=True),
        ),
    ]
