# Generated by Django 3.2.5 on 2021-07-25 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20210725_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='vehicle_documents',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
