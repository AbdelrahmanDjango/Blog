# Generated by Django 4.2.7 on 2023-12-07 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_comment_parent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Replay',
        ),
    ]
