# Generated by Django 3.1.7 on 2021-03-06 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210305_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='product',
            field=models.ManyToManyField(blank=True, to='main.Product', verbose_name='Товары'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'category')},
        ),
    ]
