# Generated by Django 4.2.7 on 2024-05-03 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0013_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='webImages')),
            ],
        ),
    ]
