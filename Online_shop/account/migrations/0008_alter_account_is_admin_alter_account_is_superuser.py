# Generated by Django 4.1.1 on 2025-03-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_account_is_admin_alter_account_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
