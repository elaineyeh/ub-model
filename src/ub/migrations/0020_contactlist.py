# Generated by Django 3.2.4 on 2021-08-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ub', '0019_alter_link_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]