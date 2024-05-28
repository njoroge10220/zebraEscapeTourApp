# Generated by Django 4.2.7 on 2024-04-05 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0009_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='viewImages')),
                ('place', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tour.place')),
            ],
        ),
    ]
