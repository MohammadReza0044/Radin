# Generated by Django 4.2 on 2023-05-06 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('national_code', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('contract_number', models.IntegerField(unique=True)),
                ('contract_type', models.CharField(choices=[('فروش', 'فروش'), ('حق العملکاری', 'حق العملکاری')], max_length=50)),
                ('car_type', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('در حال انجام', 'در حال انجام'), ('تمام شده', 'تمام شده'), ('تاخیر خورده', 'تاخیر خورده'), ('تمدید شده', 'تمدید شده')], max_length=50)),
            ],
            options={
                'db_table': 'Contract',
                'ordering': ('-created_date',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='contract/images')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='contract.contract')),
            ],
            options={
                'db_table': 'Contract Photos',
            },
        ),
    ]
