# Generated by Django 3.2.3 on 2021-05-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=256)),
                ('image', models.CharField(max_length=256)),
                ('stock', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=32)),
            ],
        ),
    ]
