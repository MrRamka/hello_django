# Generated by Django 2.2 on 2019-04-06 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_choice_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
