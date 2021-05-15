# Generated by Django 3.2.2 on 2021-05-14 12:51

from django.db import migrations, models
import djlime.utils


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_portfolio_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=djlime.utils.get_file_path, verbose_name='main image'),
        ),
    ]
