# Generated by Django 3.0.5 on 2020-08-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200825_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='content',
        ),
        migrations.AddField(
            model_name='product',
            name='content_additional',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='content_ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='content_recipe',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, default='XXX'),
            preserve_default=False,
        ),
    ]
