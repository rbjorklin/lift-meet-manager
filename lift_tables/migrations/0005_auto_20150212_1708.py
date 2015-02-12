# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lift_tables', '0004_auto_20150212_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lifter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sur_name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LifterMeta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('weight', models.FloatField(default=0)),
                ('weight_unit', models.CharField(max_length=3)),
                ('height', models.FloatField(default=0)),
                ('height_unit', models.CharField(max_length=3)),
                ('club', models.CharField(max_length=30)),
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
                ('competition', models.ForeignKey(to='lift_tables.Competition')),
                ('lifter', models.ForeignKey(to='lift_tables.Lifter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='powerlifter',
            name='competition',
        ),
        migrations.DeleteModel(
            name='PowerLifter',
        ),
        migrations.RemoveField(
            model_name='weightlifter',
            name='competition',
        ),
        migrations.DeleteModel(
            name='WeightLifter',
        ),
    ]
