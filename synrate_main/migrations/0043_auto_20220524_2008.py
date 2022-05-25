# Generated by Django 3.2.9 on 2022-05-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synrate_main', '0042_auto_20220524_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_type', models.CharField(choices=[('right', 'Баннер справа'), ('top', 'Баннер сверху'), ('bottom', 'Баннер снизу')], default='right', max_length=50, verbose_name='тип банера')),
                ('code', models.TextField(verbose_name='Код банера')),
            ],
        ),
        migrations.AlterField(
            model_name='searchquery',
            name='search_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество запросов'),
        ),
    ]