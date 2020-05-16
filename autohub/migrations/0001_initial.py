# Generated by Django 3.0.5 on 2020-05-02 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField()),
                ('established', models.DateField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('description', models.TextField()),
                ('established', models.DateField()),
                ('cover', models.URLField(null=True)),
                ('cover2', models.URLField(null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('brand_name', models.CharField(max_length=50, null=True)),
                ('car_type_name', models.CharField(max_length=50, null=True)),
                ('fuel', models.CharField(choices=[('diesel', 'DIESEL'), ('unleaded95', 'UNLEADED95')], max_length=100, null=True)),
                ('transmission', models.CharField(choices=[('manual', 'MANUAL'), ('automatic', 'AUTOMATIC')], max_length=100, null=True)),
                ('year', models.CharField(choices=[('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')], max_length=100, null=True)),
                ('country', models.CharField(max_length=20, null=True)),
                ('price', models.CharField(max_length=15, null=True)),
                ('description', models.TextField()),
                ('cover', models.URLField(null=True)),
                ('cover1', models.URLField(null=True)),
                ('video', models.URLField(null=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autohub.Manufacturer')),
                ('car_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autohub.CarType')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]