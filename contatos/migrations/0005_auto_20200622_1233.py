# Generated by Django 3.0.7 on 2020-06-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_auto_20200620_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
