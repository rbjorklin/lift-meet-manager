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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('competition_date', models.DateField()),
                ('competition_type', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PowerLifter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sur_name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('weight', models.FloatField(default=0)),
                ('weight_unit', models.CharField(max_length=3)),
                ('height', models.FloatField(default=0)),
                ('height_unit', models.CharField(max_length=3)),
                ('club', models.CharField(max_length=30)),
                ('squat_rack_height', models.IntegerField(default=0)),
                ('bench_rack_height', models.IntegerField(default=0)),
                ('bench_safety_height', models.IntegerField(default=0)),
                ('squat1', models.FloatField(default=0)),
                ('squat2', models.FloatField(default=0)),
                ('squat3', models.FloatField(default=0)),
                ('bench1', models.FloatField(default=0)),
                ('bench2', models.FloatField(default=0)),
                ('bench3', models.FloatField(default=0)),
                ('deadlift1', models.FloatField(default=0)),
                ('deadlift2', models.FloatField(default=0)),
                ('deadlift3', models.FloatField(default=0)),
                ('competition', models.ForeignKey(to='lift_tables.Competition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weight_lifter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sur_name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('weight', models.FloatField(default=0)),
                ('weight_unit', models.CharField(max_length=3)),
                ('height', models.FloatField(default=0)),
                ('height_unit', models.CharField(max_length=3)),
                ('club', models.CharField(max_length=30)),
                ('snatch1', models.FloatField(default=0)),
                ('snatch2', models.FloatField(default=0)),
                ('snatch3', models.FloatField(default=0)),
                ('clean1', models.FloatField(default=0)),
                ('clean2', models.FloatField(default=0)),
                ('clean3', models.FloatField(default=0)),
                ('competition', models.ForeignKey(to='lift_tables.Competition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
