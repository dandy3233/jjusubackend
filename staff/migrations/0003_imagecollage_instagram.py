# Generated by Django 5.1.3 on 2024-12-03 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_imagecollage_alter_staffmember_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecollage',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
    ]
