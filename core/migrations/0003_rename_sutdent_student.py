# Generated by Django 4.0.5 on 2022-06-14 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_sutdent_roll'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sutdent',
            new_name='student',
        ),
    ]
