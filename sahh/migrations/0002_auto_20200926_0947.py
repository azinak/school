# Generated by Django 3.1.1 on 2020-09-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='staffs',
            name='phone',
            field=models.TextField(default='000000'),
        ),
        migrations.AddField(
            model_name='students',
            name='phone',
            field=models.TextField(default='000000'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone',
            field=models.TextField(default='000000'),
        ),
    ]