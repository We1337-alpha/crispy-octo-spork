# Generated by Django 5.0.7 on 2024-07-19 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_posts_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Category',
            new_name='category',
        ),
    ]
