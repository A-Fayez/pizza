# Generated by Django 3.0.6 on 2020-06-10 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_menuitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='small_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]
