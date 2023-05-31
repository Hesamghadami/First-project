# Generated by Django 4.1.7 on 2023-05-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='empty', max_length=255)),
                ('image', models.ImageField(default='default2.jpg', upload_to='images')),
                ('link', models.CharField(default='#', max_length=255)),
            ],
        ),
    ]