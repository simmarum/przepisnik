# Generated by Django 3.1 on 2020-09-08 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
        ('home', '0011_delete_rateproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_rate', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.page')),
            ],
        ),
    ]