# Generated by Django 3.0.3 on 2020-03-03 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocksbackend', '0002_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funds', models.DecimalField(decimal_places=2, max_digits=9)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='stocksbackend.Profile'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='stocksbackend.Profile'),
        ),
    ]