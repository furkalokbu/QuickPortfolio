# Generated by Django 3.2.3 on 2021-05-15 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True, verbose_name='message')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('portfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='projects.portfolio')),
            ],
        ),
    ]