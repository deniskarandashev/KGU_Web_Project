# Generated by Django 3.1.4 on 2020-12-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201213_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantsforsale',
            name='body',
            field=models.TextField(verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='plantsforsale',
            name='title',
            field=models.CharField(max_length=120, verbose_name='title'),
        ),
    ]
