# Generated by Django 4.2.7 on 2023-12-11 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_alter_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='postname',
        ),
    ]