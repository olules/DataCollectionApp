# Generated by Django 4.1.2 on 2022-10-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_constructionbuilding_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='description',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
    ]