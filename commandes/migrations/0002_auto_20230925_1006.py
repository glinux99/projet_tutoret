# Generated by Django 3.2.20 on 2023-09-25 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0001_initial'),
        ('clients', '0001_initial'),
        ('commandes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandes',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.clients'),
        ),
        migrations.AddField(
            model_name='commandes',
            name='produit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produits.produits'),
        ),
    ]