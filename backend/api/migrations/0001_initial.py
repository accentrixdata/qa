# Generated by Django 3.2.8 on 2021-10-16 07:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]