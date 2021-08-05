# Generated by Django 3.2.6 on 2021-08-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BanglaWords',
            fields=[
                ('bng_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('bangla_word', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Bangla Words',
            },
        ),
    ]