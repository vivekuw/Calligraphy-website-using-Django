# Generated by Django 5.1.4 on 2025-02-11 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_admission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
