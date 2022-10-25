# Generated by Django 4.1.2 on 2022-10-25 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_projectaffectedperson_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='crop',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='PAPLand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_no', models.CharField(blank=True, max_length=200, null=True)),
                ('tenure', models.CharField(choices=[('Mailo Land', 'Mailo Land'), ('Freehold Land', 'Freehold Land'), ('Lease Land', 'Lease Land'), ('Customary Land', 'Customer Land')], max_length=20)),
                ('size', models.PositiveBigIntegerField()),
                ('location', models.CharField(max_length=255)),
                ('land_use', models.TextField(blank=True, null=True)),
                ('land_services', models.TextField(blank=True, null=True)),
                ('rate', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='land_owners', to='api.projectaffectedperson')),
                ('type_of_land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pap_land', to='api.land')),
            ],
        ),
    ]
