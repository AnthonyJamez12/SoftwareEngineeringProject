# Generated by Django 3.2.14 on 2023-04-01 20:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_alter_newmovie_age_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickets', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10)])),
                ('seats', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10)])),
                ('start_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movie')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.theater')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
