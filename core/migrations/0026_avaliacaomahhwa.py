# Generated by Django 5.1.3 on 2024-12-17 18:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0025_user_tipo_usuario_alter_user_foto"),
    ]

    operations = [
        migrations.CreateModel(
            name="AvaliacaoMahhwa",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "puntuacao",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
                ("comentario", models.TextField(blank=True, null=True)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                (
                    "manhwa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="avaliacoes", to="core.manhwa"
                    ),
                ),
            ],
        ),
    ]