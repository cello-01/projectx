# Generated by Django 4.2.2 on 2023-06-08 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_question',
            name='option_3',
        ),
        migrations.RemoveField(
            model_name='add_question',
            name='option_4',
        ),
    ]
