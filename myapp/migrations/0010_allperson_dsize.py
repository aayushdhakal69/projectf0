# Generated by Django 4.1.7 on 2023-06-07 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_allperson_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='allperson',
            name='dsize',
            field=models.CharField(default='5.5', max_length=4),
        ),
    ]
