# Generated by Django 3.2.9 on 2022-05-24 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('synrate_main', '0044_banner_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Банер', 'verbose_name_plural': 'Банеры'},
        ),
    ]