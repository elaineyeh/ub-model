# Generated by Django 3.2.2 on 2021-05-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ub', '0003_auto_20210508_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='google_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
