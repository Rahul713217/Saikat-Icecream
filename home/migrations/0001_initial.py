# Generated by Django 4.0.2 on 2022-04-13 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=22)),
                ('desc', models.TextField()),
                ('file', models.FileField()),
                ('date', models.DateField()),
            ],
        ),
    ]
