# Generated by Django 5.0.1 on 2024-01-29 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homiy',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='homiy',
            name='email',
        ),
        migrations.RemoveField(
            model_name='homiy',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='homiy',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='homiy',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='homiy',
            name='username',
        ),
        migrations.AlterField(
            model_name='homiy',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date created'),
        ),
    ]