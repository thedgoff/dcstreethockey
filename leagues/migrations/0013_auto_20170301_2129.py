# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-02 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0012_auto_20170301_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('notes', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('is_postseason', models.BooleanField(default=False)),
                ('awayteam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='leagues.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='awayteam',
        ),
        migrations.RemoveField(
            model_name='game',
            name='hometeam',
        ),
        migrations.RemoveField(
            model_name='game',
            name='is_postseason',
        ),
        migrations.RemoveField(
            model_name='game',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='game',
            name='ref1',
        ),
        migrations.RemoveField(
            model_name='game',
            name='ref2',
        ),
        migrations.RemoveField(
            model_name='game',
            name='time',
        ),
        migrations.RemoveField(
            model_name='ref',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='ref',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='stat',
            name='game',
        ),
        migrations.AddField(
            model_name='game',
            name='gamenumber',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='matchup',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leagues.Game'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='hometeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='leagues.Team'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='ref1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='leagues.Ref'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='ref2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='leagues.Ref'),
        ),
        migrations.AddField(
            model_name='stat',
            name='matchup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leagues.MatchUp'),
        ),
    ]
