# Generated by Django 3.1.2 on 2020-10-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201012_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.ImageField(null=True, upload_to='%Y/%m/%d'),
        ),
    ]