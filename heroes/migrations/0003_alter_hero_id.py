# Generated by Django 5.0 on 2024-01-18 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0002_alter_hero_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
