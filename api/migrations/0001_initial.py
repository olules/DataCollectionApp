# Generated by Django 4.1.2 on 2022-10-06 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.crop')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAffectedPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('age', models.PositiveIntegerField()),
                ('National_id_no', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('phone_number', models.PositiveIntegerField()),
                ('crops', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.crop')),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.land')),
            ],
        ),
    ]
