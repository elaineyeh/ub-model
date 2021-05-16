# Generated by Django 3.2.2 on 2021-05-10 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ub', '0006_state_label'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FastLink',
            new_name='Link',
        ),
        migrations.RenameModel(
            old_name='ActivityCategory',
            new_name='Role',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='activity_category',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='subscribe',
            new_name='subscribed',
        ),
    ]