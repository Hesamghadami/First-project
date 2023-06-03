# Generated by Django 4.1.7 on 2023-06-03 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('which_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comments')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]