# Generated by Django 4.1.2 on 2022-10-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_remove_projectaffectedperson_quantity_of_crops_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectaffectedperson',
            name='id_no',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
