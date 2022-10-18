# Generated by Django 3.2.4 on 2021-06-11 03:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('total', models.FloatField()),
                ('troco', models.CharField(blank=True, max_length=20)),
                ('pagamento', models.CharField(max_length=20)),
                ('ponto_referencia', models.CharField(blank=True, max_length=2000)),
                ('data', models.DateTimeField(default=datetime.datetime(2021, 6, 11, 3, 43, 25, 799822))),
                ('cep', models.CharField(blank=True, max_length=50)),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(blank=True, max_length=200)),
                ('telefone', models.CharField(max_length=30)),
                ('entregue', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
                ('adicionais', models.TextField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
    ]