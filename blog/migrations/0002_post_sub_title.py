# Generated by Django 2.0.13 on 2019-05-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sub_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
