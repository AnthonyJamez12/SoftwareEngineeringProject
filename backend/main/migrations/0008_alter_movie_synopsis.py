# Generated by Django 3.2.14 on 2023-03-29 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20230329_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
