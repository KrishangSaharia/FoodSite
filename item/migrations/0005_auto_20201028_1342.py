# Generated by Django 3.1.2 on 2020-10-28 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20201028_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='combo',
            old_name='photo',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='photo',
            new_name='image',
        ),
    ]