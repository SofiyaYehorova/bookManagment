# Generated by Django 5.0.4 on 2024-04-10 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_bookmodel_isbn'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bookmodel',
            table='books',
        ),
    ]