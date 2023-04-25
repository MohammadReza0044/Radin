# Generated by Django 4.2 on 2023-04-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_todolist_options_alter_todolist_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Manager Message',
                'ordering': ('-created',),
                'get_latest_by': 'created',
            },
        ),
    ]
