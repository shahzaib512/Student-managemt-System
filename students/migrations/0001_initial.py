# Generated by Django 5.0.8 on 2024-08-07 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('RegistrationNo', models.CharField(max_length=100)),
                ('Email', models.EmailField(blank=True, max_length=100, unique=True)),
                ('Cource', models.CharField(max_length=100)),
            ],
        ),
    ]
