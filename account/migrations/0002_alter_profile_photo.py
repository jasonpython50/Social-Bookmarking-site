# Generated by Django 3.2.5 on 2021-07-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='no_photo.jpg', upload_to='users/%Y/%m/%d/'),
        ),
    ]
