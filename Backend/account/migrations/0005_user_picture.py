# Generated by Django 4.2 on 2023-04-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_vacation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(null=True, upload_to='users/image'),
        ),
    ]
