# Generated by Django 3.2.9 on 2022-03-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synrate_main', '0015_auto_20220322_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=600, null=True, verbose_name='Название'),
        ),
    ]