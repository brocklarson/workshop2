# Generated by Django 3.2.2 on 2023-04-29 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20230427_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(),
        ),
    ]
