# Generated by Django 3.1.4 on 2020-12-09 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tagline', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('Eng', 'English'), ('Ar', 'Arabic'), ('Fr', 'French'), ('Hindi', 'Hindi'), ('Ch', 'Chineese')], max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('icon', models.URLField()),
                ('image', models.URLField()),
                ('isDisliked', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RadioOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio_api.radio')),
            ],
        ),
    ]
