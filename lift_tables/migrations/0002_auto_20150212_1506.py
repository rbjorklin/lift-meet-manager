# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lift_tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightLifter',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
        migrations.RemoveField(
            model_name='weight_lifter',
            name='competition',
        ),
        migrations.DeleteModel(
            name='Weight_lifter',
        ),
    ]
