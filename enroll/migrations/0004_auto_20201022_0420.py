# Generated by Django 3.1.2 on 2020-10-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_auto_20201022_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]