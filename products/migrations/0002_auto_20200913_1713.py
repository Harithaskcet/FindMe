# Generated by Django 2.2.15 on 2020-09-13 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='icon',
            new_name='iconImage',
        ),
    ]
