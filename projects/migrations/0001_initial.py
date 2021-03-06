# Generated by Django 3.2.3 on 2021-05-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('show', models.BooleanField(default=True, verbose_name='show')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, upload_to='portfolio/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'ordering': ('created_at',),
            },
        ),
    ]
