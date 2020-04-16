# Generated by Django 3.0.4 on 2020-04-15 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_panels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panels',
            name='fk',
        ),
        migrations.AlterField(
            model_name='panels',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.services'),
        ),
    ]