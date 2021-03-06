# Generated by Django 3.0.4 on 2020-04-16 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20200416_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='svcitems',
            name='title',
            field=models.CharField(default=12, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='svcitems',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myService', to='basic_app.services'),
        ),
    ]
