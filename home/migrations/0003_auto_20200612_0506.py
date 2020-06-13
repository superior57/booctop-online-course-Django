# Generated by Django 3.0.6 on 2020-06-12 05:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('home', '0002_auto_20200612_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 12, 5, 6, 22, 756116, tzinfo=utc), verbose_name='date joined'),
        ),
        migrations.DeleteModel(
            name='user_groups',
        ),
    ]
