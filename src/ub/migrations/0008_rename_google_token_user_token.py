# Generated by Django 3.2.2 on 2021-05-10 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ub', '0007_auto_20210510_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='google_token',
            new_name='token',
        ),
    ]
