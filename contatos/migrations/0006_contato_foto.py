# Generated by Django 3.0.7 on 2020-06-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0005_auto_20200622_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='foto/%Y/%m/%d'),
        ),
    ]