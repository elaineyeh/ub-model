# Generated by Django 3.2.2 on 2021-05-08 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ub.state'),
        ),
    ]