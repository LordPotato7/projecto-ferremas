# Generated by Django 5.0.6 on 2024-06-04 00:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now=True)),
                ('precio', models.IntegerField()),
                ('precio_oferta', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos oferta')),
                ('stock', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.marca')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('stock', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.marca')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo')),
            ],
        ),
    ]