from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('nome', 'categoria')
    search_fields = ('nome',)
    list_editable = ('telefone', 'mostrar')

# Register your models here.


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
