# Generated by Django 4.1.2 on 2022-10-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_rename_pap_name_papland_pap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papland',
            name='tenure',
            field=models.CharField(choices=[('Mailo Land', 'Mailo Land'), ('Freehold Land', 'Freehold Land'), ('Lease Land', 'Lease Land'), ('Customary Land', 'Customary Land')], max_length=20),
        ),
    ]
