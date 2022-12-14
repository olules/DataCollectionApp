# Generated by Django 4.1.2 on 2022-10-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_tree_projectaffectedperson_trees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectaffectedperson',
            name='construction_type',
        ),
        migrations.RemoveField(
            model_name='projectaffectedperson',
            name='trees',
        ),
        migrations.RemoveField(
            model_name='projectaffectedperson',
            name='type_of_crops',
        ),
        migrations.RemoveField(
            model_name='projectaffectedperson',
            name='type_of_land',
        ),
        migrations.AddField(
            model_name='projectaffectedperson',
            name='construction_type',
            field=models.ManyToManyField(to='api.constructionbuilding'),
        ),
        migrations.AddField(
            model_name='projectaffectedperson',
            name='trees',
            field=models.ManyToManyField(blank=True, null=True, to='api.tree'),
        ),
        migrations.AddField(
            model_name='projectaffectedperson',
            name='type_of_crops',
            field=models.ManyToManyField(to='api.crop'),
        ),
        migrations.AddField(
            model_name='projectaffectedperson',
            name='type_of_land',
            field=models.ManyToManyField(to='api.land'),
        ),
    ]
