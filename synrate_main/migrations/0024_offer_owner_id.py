# Generated by Django 3.2.9 on 2022-04-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synrate_main', '0023_offer_short_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='owner_id',
            field=models.IntegerField(blank=True, db_index=True, default=None, null=True),
        ),
    ]
