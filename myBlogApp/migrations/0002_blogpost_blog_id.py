# Generated by Django 4.2.10 on 2024-03-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blog_id',
            field=models.IntegerField(null=True),
        ),
    ]