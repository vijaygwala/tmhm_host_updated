# Generated by Django 3.0.7 on 2020-07-16 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facilitators', '0004_facilitator'),
        ('LandingPage', '0002_auto_20200714_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='Fid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facilitators.Facilitator'),
        ),
    ]