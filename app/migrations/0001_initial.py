# Generated by Django 4.1.4 on 2023-08-14 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=120)),
                ('contact', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.FileField(upload_to='profile')),
                ('aadharcard', models.FileField(upload_to='aadharcard')),
                ('pancard', models.FileField(upload_to='pancard')),
                ('marksheet', models.FileField(upload_to='marksheet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person')),
            ],
        ),
    ]