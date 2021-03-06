# Generated by Django 3.2.3 on 2021-05-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20210517_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.TextField(default='', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
