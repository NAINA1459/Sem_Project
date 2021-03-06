# Generated by Django 3.1.7 on 2021-04-20 17:31

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('first', models.CharField(max_length=50)),
                ('last', models.CharField(default='', max_length=70)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('email', models.CharField(default='', max_length=70)),
                ('youtube', models.URLField(max_length=250)),
                ('instagram', models.URLField(max_length=250)),
                ('facebook', models.URLField(max_length=250)),
                ('snapchat', models.URLField(max_length=250)),
                ('cat1', models.CharField(default='none', max_length=70)),
                ('cat2', models.CharField(default='none', max_length=70)),
                ('cat3', models.CharField(default='none', max_length=70)),
                ('cat4', models.CharField(default='none', max_length=70)),
            ],
        ),
    ]
