# Generated by Django 2.0.4 on 2018-04-29 14:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HoldApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 4, 29, 14, 36, 45, 332455, tzinfo=utc))),
                ('mod_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='report',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 29, 14, 36, 45, 333503, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='data',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HoldApp.Report'),
        ),
    ]