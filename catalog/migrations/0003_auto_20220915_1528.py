# Generated by Django 3.1.14 on 2022-09-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20220915_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='archived',
            field=models.BooleanField(),
        ),
    ]
