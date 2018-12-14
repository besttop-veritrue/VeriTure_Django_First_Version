# Generated by Django 2.0.4 on 2018-12-14 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20170416_1821'),
        ('certviewer', '0003_auto_20181214_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Account'),
            preserve_default=False,
        ),
    ]