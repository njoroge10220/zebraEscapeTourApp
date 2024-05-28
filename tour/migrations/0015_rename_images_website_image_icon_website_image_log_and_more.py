# Generated by Django 4.2.7 on 2024-05-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0014_website_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='website_image',
            old_name='images',
            new_name='Icon',
        ),
        migrations.AddField(
            model_name='website_image',
            name='Log',
            field=models.ImageField(null=True, upload_to='webImages'),
        ),
        migrations.AddField(
            model_name='website_image',
            name='Name',
            field=models.ImageField(null=True, upload_to='webImages'),
        ),
    ]