# Generated by Django 3.1.14 on 2022-09-15 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20220915_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.supplier'),
        ),
    ]
