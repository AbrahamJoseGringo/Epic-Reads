"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import Autor, AvaliacaoLivro, AvaliacaoMahhwa, Categoria, Compra, Editora, ItensCompra, Livro, Manhwa, Tipo, User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name", "foto", "tipo_usuario", "passage_id")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
        (_("Groups"), {"fields": ("groups",)}),
        (_("User Permissions"), {"fields": ("user_permissions",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome', 'email')
    list_per_page = 10

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 10

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cidade')
    search_fields = ('nome', 'email', 'cidade')
    list_filter = ('nome', 'email', 'cidade')
    ordering = ('nome', 'email', 'cidade')
    list_per_page = 10

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'categoria', 'tipo')
    search_fields = ('titulo', 'editora__nome', 'categoria__descricao', 'tipo_descricao')
    list_filter = ('editora', 'categoria', 'tipo')
    ordering = ('titulo', 'editora', 'categoria', 'tipo')
    list_per_page = 10

@admin.register(Manhwa)
class ManhwaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'tipo')
    search_fields = ('titulo', 'categoria__descricao', 'tipo_descricao')
    list_filter = ('categoria', 'tipo')
    ordering = ('titulo', 'categoria', 'tipo')
    list_per_page = 10

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 10

class ItensCompraInline(admin.StackedInline):  # opção: TabularInline
    model = ItensCompra
    extra = 1  # Quantidade de itens adicionais


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("usuario", "status")
    search_fields = ("usuario", "status")
    list_filter = ("usuario", "status")
    ordering = ("usuario", "status")
    list_per_page = 25
    inlines = [ItensCompraInline]

@admin.register(AvaliacaoLivro)
class AvaliacaoLivroAdmin(admin.ModelAdmin):
    list_display = ('livro', 'puntuacao', 'comentario', 'criado_em')
    search_fields = ('livro__titulo', 'comentario')
    list_filter = ('puntuacao', 'criado_em')
    ordering = ('livro', 'puntuacao')
    list_per_page = 10    

@admin.register(AvaliacaoMahhwa)
class AvaliacaoManhwaAdmin(admin.ModelAdmin):
    list_display = ('manhwa', 'puntuacao', 'comentario', 'criado_em')
    search_fields = ('manhwa__titulo', 'comentario')
    list_filter = ('puntuacao', 'criado_em')
    ordering = ('manhwa', 'puntuacao')
    list_per_page = 10    
