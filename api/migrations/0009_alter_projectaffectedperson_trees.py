# Generated by Django 4.1.2 on 2022-10-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_projectaffectedperson_construction_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectaffectedperson',
            name='trees',
            field=models.ManyToManyField(blank=True, to='api.tree'),
        ),
    ]
