
# Generated by Django 3.2.3 on 2021-12-23 11:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='make',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='make',
            name='name',
            field=models.CharField(help_text='Enter a make: ', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greateer than 1 character')]),
        ),
    ]
