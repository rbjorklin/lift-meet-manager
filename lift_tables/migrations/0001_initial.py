# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('type', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30, default='N/A')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lifter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('sur_name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('date', models.DateField()),
                ('weight', models.FloatField(default=0)),
                ('weight_unit', models.CharField(max_length=3, default='kg')),
                ('height', models.FloatField(default=0)),
                ('height_unit', models.CharField(max_length=3, default='cm')),
                ('club', models.CharField(blank=True, max_length=30)),
                ('squat_rack_height', models.IntegerField(default=0)),
                ('bench_rack_height', models.IntegerField(default=0)),
                ('bench_safety_height', models.IntegerField(default=0)),
                ('lift1_attempt1', models.FloatField(default=0)),
                ('lift1_attempt1_left_judge', models.NullBooleanField()),
                ('lift1_attempt1_center_judge', models.NullBooleanField()),
                ('lift1_attempt1_right_judge', models.NullBooleanField()),
                ('lift1_attempt2', models.FloatField(default=0)),
                ('lift1_attempt2_left_judge', models.NullBooleanField()),
                ('lift1_attempt2_center_judge', models.NullBooleanField()),
                ('lift1_attempt2_right_judge', models.NullBooleanField()),
                ('lift1_attempt3', models.FloatField(default=0)),
                ('lift1_attempt3_left_judge', models.NullBooleanField()),
                ('lift1_attempt3_center_judge', models.NullBooleanField()),
                ('lift1_attempt3_right_judge', models.NullBooleanField()),
                ('lift2_attempt1', models.FloatField(default=0)),
                ('lift2_attempt1_left_judge', models.NullBooleanField()),
                ('lift2_attempt1_center_judge', models.NullBooleanField()),
                ('lift2_attempt1_right_judge', models.NullBooleanField()),
                ('lift2_attempt2', models.FloatField(default=0)),
                ('lift2_attempt2_left_judge', models.NullBooleanField()),
                ('lift2_attempt2_center_judge', models.NullBooleanField()),
                ('lift2_attempt2_right_judge', models.NullBooleanField()),
                ('lift2_attempt3', models.FloatField(default=0)),
                ('lift2_attempt3_left_judge', models.NullBooleanField()),
                ('lift2_attempt3_center_judge', models.NullBooleanField()),
                ('lift2_attempt3_right_judge', models.NullBooleanField()),
                ('lift3_attempt1', models.FloatField(default=0)),
                ('lift3_attempt1_left_judge', models.NullBooleanField()),
                ('lift3_attempt1_center_judge', models.NullBooleanField()),
                ('lift3_attempt1_right_judge', models.NullBooleanField()),
                ('lift3_attempt2', models.FloatField(default=0)),
                ('lift3_attempt2_left_judge', models.NullBooleanField()),
                ('lift3_attempt2_center_judge', models.NullBooleanField()),
                ('lift3_attempt2_right_judge', models.NullBooleanField()),
                ('lift3_attempt3', models.FloatField(default=0)),
                ('lift3_attempt3_left_judge', models.NullBooleanField()),
                ('lift3_attempt3_center_judge', models.NullBooleanField()),
                ('lift3_attempt3_right_judge', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='competition',
            name='participants',
            field=models.ManyToManyField(blank=True, to='lift_tables.Lifter'),
            preserve_default=True,
        ),
    ]
