# Generated by Django 3.1.6 on 2021-02-14 06:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20210214_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogitem',
            name='blog_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='blogitem',
            name='category',
            field=models.CharField(choices=[('Tips', 'Tips'), ('Business', 'Business'), ('Lifestyle', 'Lifestyle'), ('Beauty', 'Beauty')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blogitem',
            name='post_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 2, 14, 6, 52, 6, 576925, tzinfo=utc)),
        ),
    ]
