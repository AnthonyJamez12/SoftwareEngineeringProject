# Generated by Django 3.2.14 on 2023-03-29 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20230329_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='cast',
        ),
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.cast'),
        ),
    ]
