# Generated by Django 3.2.16 on 2024-03-10 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cont_us', '0012_service_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='thumbnail_white',
            field=models.ImageField(default=1, upload_to='Service/white'),
            preserve_default=False,
        ),
    ]