# Generated by Django 2.0.4 on 2018-12-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certviewer', '0002_auto_20181214_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='signatureImg',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificate',
            name='subtitle',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]
