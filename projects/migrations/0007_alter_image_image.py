# Generated by Django 3.2.3 on 2021-05-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20210516_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='', upload_to='portfolio/%Y/%m/%d/'),
        ),
    ]
