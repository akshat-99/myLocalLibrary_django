# Generated by Django 2.1.5 on 2020-03-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a book genre (e.g. Science, Fiction)', max_length=200),
        ),
    ]
