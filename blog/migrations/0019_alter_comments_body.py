# Generated by Django 4.0.6 on 2022-07-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_comments_reply_alter_comments_reply_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
