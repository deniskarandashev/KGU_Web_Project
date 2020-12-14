# Generated by Django 3.1.4 on 2020-12-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201213_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=120, verbose_name='title1')),
                ('title2', models.CharField(max_length=120, verbose_name='title2')),
                ('body', models.TextField(verbose_name='text')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Other Article',
                'verbose_name_plural': 'Other Articles',
            },
        ),
        migrations.CreateModel(
            name='PlantsForSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title1')),
                ('body', models.TextField(verbose_name='text')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='price')),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Head Article',
                'verbose_name_plural': 'Head Articles',
            },
        ),
        migrations.DeleteModel(
            name='MainArticle',
        ),
        migrations.DeleteModel(
            name='OtherArticle',
        ),
    ]
