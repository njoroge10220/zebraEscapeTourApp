# Generated by Django 4.2.7 on 2024-04-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0007_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='Image',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='viewImages'),
        ),
    ]
