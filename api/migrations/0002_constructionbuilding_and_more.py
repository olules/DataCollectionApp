# Generated by Django 4.1.2 on 2022-10-06 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructionBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='projectaffectedperson',
            name='construction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.constructionbuilding'),
            preserve_default=False,
        ),
    ]
