# Generated by Django 3.2.4 on 2021-06-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ub', '0012_state_prompt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_id', models.IntegerField()),
                ('activity_name', models.CharField(max_length=64)),
                ('unit_name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=8)),
                ('apply_qualification_list', models.JSONField()),
                ('apply_start_date', models.DateTimeField()),
                ('apply_start_time', models.DateTimeField()),
                ('apply_end_date', models.DateTimeField()),
                ('apply_end_time', models.DateTimeField()),
                ('post_start_time', models.DateTimeField()),
                ('post_end_time', models.DateTimeField()),
                ('activity_start_time', models.DateTimeField()),
                ('activity_end_time', models.DateTimeField()),
            ],
        ),
    ]