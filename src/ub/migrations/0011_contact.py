# Generated by Django 3.2.2 on 2021-05-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ub', '0010_auto_20210513_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_id', models.TextField()),
                ('contact', models.JSONField()),
            ],
        ),
    ]
