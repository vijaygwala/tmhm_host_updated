# Generated by Django 3.0.7 on 2020-07-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilitators', '0011_auto_20200705_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='RExperience',
            field=models.CharField(choices=[(1, '3-6 yrs'), (2, '6-10 yrs'), (3, '10+ yrs')], max_length=1),
        ),
        migrations.AlterField(
            model_name='experience',
            name='TExperience',
            field=models.CharField(choices=[(1, '3-6 yrs'), (2, '6-10 yrs'), (3, '10+ yrs')], max_length=1),
        ),
    ]
