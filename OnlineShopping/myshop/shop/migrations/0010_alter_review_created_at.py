# Generated by Django 5.0.7 on 2024-07-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
