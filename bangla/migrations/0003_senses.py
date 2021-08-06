# Generated by Django 3.2.6 on 2021-08-06 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangla', '0002_auto_20210806_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Senses',
            fields=[
                ('sense_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('synset', models.CharField(max_length=32)),
                ('eng_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangla.englishwords')),
            ],
            options={
                'verbose_name_plural': 'Senses',
            },
        ),
    ]