# Generated by Django 3.2.12 on 2023-10-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0002_train_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='start_seat',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
