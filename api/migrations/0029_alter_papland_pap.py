# Generated by Django 4.1.2 on 2022-10-28 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_alter_crop_description_alter_crop_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papland',
            name='pap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pap_lands', to='api.projectaffectedperson'),
        ),
    ]
