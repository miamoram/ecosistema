# Generated by Django 4.2 on 2023-04-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0006_residue_photo_predicted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residue',
            name='photo_predicted',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]
