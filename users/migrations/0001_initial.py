# Generated by Django 2.2.1 on 2019-05-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('company_name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('zip', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('web', models.URLField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]