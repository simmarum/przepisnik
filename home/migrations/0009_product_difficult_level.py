# Generated by Django 3.1 on 2020-09-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='difficult_level',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
