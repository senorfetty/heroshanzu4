# Generated by Django 5.0.2 on 2024-07-31 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
