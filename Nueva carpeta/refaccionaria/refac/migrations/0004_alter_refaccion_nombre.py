# Generated by Django 4.1.1 on 2022-09-21 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refac', '0003_alter_refaccion_cantidad_alter_refaccion_modelo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refaccion',
            name='nombre',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
