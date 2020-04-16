# Generated by Django 3.0.4 on 2020-04-15 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='panels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.services')),
            ],
        ),
    ]