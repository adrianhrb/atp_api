# Generated by Django 5.0.1 on 2024-01-19 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hand', models.CharField(choices=[('R', 'right'), ('L', 'left')], max_length=1)),
                ('country', models.CharField(max_length=3)),
                ('birthdate', models.DateField()),
            ],
        ),
    ]