# Generated by Django 2.2.6 on 2020-01-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=75)),
                ('edition', models.IntegerField()),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
