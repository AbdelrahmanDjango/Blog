# Generated by Django 4.2.7 on 2023-12-08 06:28

from django.db import migrations, models
import django.db.models.deletion
import polymorphic_tree.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('posts', '0015_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'base_manager_name': 'objects', 'ordering': ('tree_id', 'lft')},
        ),
        migrations.AddField(
            model_name='comment',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=polymorphic_tree.models.PolymorphicTreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='posts.comment', verbose_name='parent'),
        ),
    ]