# Generated by Django 4.2.6 on 2023-11-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_diary_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
