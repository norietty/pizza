# Generated by Django 3.0.3 on 2020-06-15 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subs',
            name='extras',
        ),
    ]
