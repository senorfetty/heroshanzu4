# Generated by Django 5.0.7 on 2024-08-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_admission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='parent_relation',
            field=models.CharField(choices=[('parent', 'Parent'), ('guardian', 'Guardian'), ('other', 'Other')], max_length=20),
        ),
    ]
