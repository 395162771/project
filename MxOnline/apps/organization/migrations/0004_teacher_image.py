# Generated by Django 2.1 on 2018-08-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180823_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', max_length=200, upload_to='teacher/%Y/%m', verbose_name='头像'),
        ),
    ]
