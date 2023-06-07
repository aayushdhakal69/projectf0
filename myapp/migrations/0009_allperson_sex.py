# Generated by Django 4.1.7 on 2023-06-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_allperson_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='allperson',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=1),
        ),
    ]
