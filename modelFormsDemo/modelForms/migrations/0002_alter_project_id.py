# Generated by Django 4.0.1 on 2022-01-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelForms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
