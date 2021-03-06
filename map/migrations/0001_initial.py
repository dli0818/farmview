# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vizjson_url', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('optional_note', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Datafield',
            fields=[
                ('datafield_id', models.AutoField(primary_key=True, serialize=False)),
                ('datafield_type', models.CharField(choices=[(b'text', b'Text'), (b'range', b'Range'), (b'select_one', b'Select One'), (b'select_multiple', b'Select Multiple')], max_length=20)),
                ('datafield_name', models.CharField(max_length=60)),
                ('datafield_label_eng', models.CharField(max_length=30)),
                ('datafield_label_esp', models.CharField(blank=True, max_length=30)),
                ('data_sources', models.TextField()),
                ('enabled', models.BooleanField(default=True)),
                ('query_choices_vals', models.TextField(blank=True)),
                ('query_choices_labels_eng', models.TextField(blank=True)),
                ('query_choices_labels_esp', models.TextField(blank=True)),
                ('use_for_query_ui', models.BooleanField(default=False)),
                ('use_for_detail_popup', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('formdata_id', models.AutoField(primary_key=True, serialize=False)),
                ('import_id', models.IntegerField()),
                ('ona_id', models.IntegerField()),
                ('dropbox_url', models.CharField(max_length=100)),
                ('last_synced_date', models.DateTimeField(auto_now=True)),
                ('current', models.BooleanField(default=True)),
                ('optional_note', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
