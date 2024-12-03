# Generated by Django 5.1.3 on 2024-12-03 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0024_livro_completo_alter_livro_capa_and_more"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="tipo_usuario",
            field=models.IntegerField(
                choices=[(1, "Cliente"), (2, "Vendedor"), (3, "Gerente")], default=1, verbose_name="User Type"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="foto",
            field=models.ForeignKey(
                blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to="uploader.image"
            ),
        ),
    ]