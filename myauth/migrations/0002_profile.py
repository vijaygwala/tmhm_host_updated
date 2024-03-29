# Generated by Django 3.0.7 on 2020-07-14 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(blank=True, max_length=30)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Learner'), (2, 'Facilitator'), (3, 'Admin')], null=True)),
                ('phone', models.CharField(max_length=13)),
                ('portfolio', models.FileField(upload_to='uploads/')),
                ('profile', models.ImageField(default='default.png', upload_to='Mentor_profiles/')),
                ('intrest', models.CharField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
