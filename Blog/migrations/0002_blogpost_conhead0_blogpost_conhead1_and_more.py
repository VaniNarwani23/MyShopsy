# Generated by Django 4.2.2 on 2024-06-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='ConHead0',
            field=models.CharField(default='', max_length=50000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='ConHead1',
            field=models.CharField(default='', max_length=50000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='ConHead2',
            field=models.CharField(default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='Head0',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='Head1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='Head2',
            field=models.CharField(default='', max_length=500),
        ),
    ]
