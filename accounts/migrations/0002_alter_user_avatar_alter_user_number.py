# Generated by Django 4.0.1 on 2022-01-31 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
    ]