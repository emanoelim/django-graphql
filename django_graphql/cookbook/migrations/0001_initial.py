# Generated by Django 3.1.7 on 2021-03-28 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('receita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.receita')),
                ('unidade_medida', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cookbook.unidademedida')),
            ],
        ),
    ]
