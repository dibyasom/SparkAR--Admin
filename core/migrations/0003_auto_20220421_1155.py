# Generated by Django 3.2.7 on 2022-04-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220421_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='laptopn_w_min_requirements',
            new_name='laptop_w_min_requirements',
        ),
        migrations.AlterField(
            model_name='applicant',
            name='whatToLearn',
            field=models.CharField(blank=True, default='', max_length=5000),
        ),
    ]