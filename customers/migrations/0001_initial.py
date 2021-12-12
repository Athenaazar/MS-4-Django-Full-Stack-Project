# Generated by Django 3.2.9 on 2021-12-12 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('address_1', models.CharField(blank=True, max_length=100, null=True)),
                ('address_2', models.CharField(blank=True, max_length=100, null=True)),
                ('town', models.CharField(blank=True, max_length=60, null=True)),
                ('county', models.CharField(blank=True, max_length=60, null=True)),
                ('postcode', models.CharField(blank=True, max_length=30, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
