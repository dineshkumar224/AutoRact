# Generated by Django 4.1.1 on 2022-10-14 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KYCData', '0007_delete_image_details_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='details',
            name='id_type',
        ),
        migrations.RemoveField(
            model_name='details',
            name='img',
        ),
    ]