# Generated by Django 5.0.4 on 2024-04-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silantmashinesapp', '0004_remove_complaints_service_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='spare_parts_used',
            field=models.TextField(blank=True, help_text='Используемые запасные части', null=True),
        ),
    ]
