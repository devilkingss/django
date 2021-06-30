# Generated by Django 3.2.4 on 2021-06-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.TextField()),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('phonenumber', models.IntegerField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
