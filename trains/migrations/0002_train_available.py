# Generated by Django 3.2.12 on 2023-10-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='available',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
