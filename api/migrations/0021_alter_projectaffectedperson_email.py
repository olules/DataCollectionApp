# Generated by Django 4.1.2 on 2022-10-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_projectaffectedperson_id_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectaffectedperson',
            name='email',
            field=models.EmailField(max_length=20, unique=True),
        ),
    ]