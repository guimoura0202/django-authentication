# Generated by Django 5.1.3 on 2024-11-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_site', '0002_remove_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]
