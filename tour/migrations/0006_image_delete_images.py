# Generated by Django 4.2.7 on 2024-04-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.FileField(upload_to='viewImages')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]