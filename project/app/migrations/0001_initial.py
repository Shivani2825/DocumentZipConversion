# Generated by Django 4.1.4 on 2023-08-11 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('profile_photo', models.ImageField(upload_to='profile_photos')),
                ('aadhar_card', models.ImageField(upload_to='aadhar_photos')),
                ('pan_card', models.ImageField(upload_to='pan_card_photos')),
                ('voter_id', models.ImageField(upload_to='voter_id_photos')),
                ('marksheet', models.ImageField(upload_to='marksheet_photos')),
            ],
        ),
    ]
