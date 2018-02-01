# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('1', '\u901a\u8fc7'), ('2', '\u4e0d\u901a\u8fc7')], max_length=10)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]