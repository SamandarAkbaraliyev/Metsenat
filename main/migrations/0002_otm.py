# Generated by Django 5.0.1 on 2024-01-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': "Oliy ta'lim Muassasasi",
                'verbose_name_plural': "Oliy ta'lim Muassasalari",
            },
        ),
    ]
