# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import project.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LargeGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MiddleGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=True)),
                ('large_genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='middle_genres', to='project.LargeGenre')),
            ],
        ),
        migrations.CreateModel(
            name='Prefecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('tag_id', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=project.models.Topic.get_image_path)),
                ('large_genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.LargeGenre')),
                ('middle_genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.MiddleGenre')),
                ('prefecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Prefecture')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='middlegenre',
            name='prefecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Prefecture'),
        ),
        migrations.AddField(
            model_name='like',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Topic'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AddField(
            model_name='largegenre',
            name='prefecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Prefecture'),
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Topic'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
    ]
