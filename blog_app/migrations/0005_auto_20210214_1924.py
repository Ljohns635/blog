# Generated by Django 3.1.6 on 2021-02-14 19:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_auto_20210214_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about_me',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogitem',
            name='category',
            field=models.CharField(choices=[('Tips', 'Tips'), ('Beauty', 'Beauty'), ('Business', 'Business'), ('Lifestyle', 'Lifestyle')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blogitem',
            name='post_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 2, 14, 19, 24, 51, 832101, tzinfo=utc)),
        ),
    ]
