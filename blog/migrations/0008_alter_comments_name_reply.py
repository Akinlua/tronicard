# Generated by Django 4.0.6 on 2022-07-16 22:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comments_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comments')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
