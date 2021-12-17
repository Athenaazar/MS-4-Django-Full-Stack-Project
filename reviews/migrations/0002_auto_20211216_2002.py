# Generated by Django 3.2.9 on 2021-12-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='review',
            field=models.TextField(max_length=500),
        ),
    ]