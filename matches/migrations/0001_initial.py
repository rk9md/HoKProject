# Generated by Django 3.1.1 on 2020-10-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op_name', models.CharField(max_length=200)),
                ('op_email', models.EmailField(max_length=200)),
                ('op_number', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('money_needed', models.PositiveSmallIntegerField()),
                ('money_spending', models.PositiveSmallIntegerField()),
                ('store', models.CharField(max_length=200)),
                ('resolved', models.BooleanField()),
            ],
        ),
    ]
