# Generated by Django 3.0.1 on 2020-07-10 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200710_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='shool_id',
            new_name='school_id',
        ),
    ]
