# Generated by Django 4.1.7 on 2023-05-10 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_delete_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campingpackage',
            old_name='name',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='cheappackage',
            old_name='name',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='luxurypackage',
            old_name='name',
            new_name='city',
        ),
    ]
