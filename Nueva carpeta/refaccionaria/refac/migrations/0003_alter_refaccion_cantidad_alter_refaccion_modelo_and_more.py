# Generated by Django 4.1 on 2022-09-07 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refac', '0002_refaccion_creado_refaccion_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refaccion',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='refaccion',
            name='modelo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='refaccion',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15),
            preserve_default=False,
        ),
    ]
