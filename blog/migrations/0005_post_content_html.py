# Generated by Django 3.1.2 on 2020-10-23 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201020_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_html',
            field=models.TextField(blank=True, editable=False, verbose_name='正文html代码'),
        ),
    ]
