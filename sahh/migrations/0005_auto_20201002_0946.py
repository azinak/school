# Generated by Django 3.1.1 on 2020-10-02 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sahh', '0004_courses_enterprise_nursery_sections'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprise',
            name='time',
        ),
        migrations.AddField(
            model_name='courses',
            name='enterprise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sahh.enterprise'),
        ),
        migrations.AddField(
            model_name='nursery',
            name='time',
            field=models.CharField(choices=[(1, 'morning'), (2, 'evening')], default=1, max_length=10),
        ),
    ]