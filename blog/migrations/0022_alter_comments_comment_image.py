# Generated by Django 4.0.6 on 2022-07-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_comments_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_image',
            field=models.ImageField(default='commentpic/Tronicard.png', upload_to='commentpic/'),
        ),
    ]
