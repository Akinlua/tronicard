# Generated by Django 4.0.6 on 2022-07-17 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comments_name_reply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
