# Generated by Django 2.2.8 on 2019-12-28 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_activateusertoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='activateusertoken',
            name='eid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
