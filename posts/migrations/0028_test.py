# Generated by Django 4.2.7 on 2023-12-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0027_remove_comment_parent_replay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]
