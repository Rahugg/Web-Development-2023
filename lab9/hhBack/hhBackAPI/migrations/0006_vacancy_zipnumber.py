# Generated by Django 4.1.7 on 2023-04-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhBackAPI', '0005_alter_company_address_alter_company_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='zipNumber',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
