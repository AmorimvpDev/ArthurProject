from django.contrib import admin
from ArthurApp.models import Produto, Categoria, Fornecedor
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    #colunas que vao aparecer
    list_display = ['id', 'nome', 'preco', 'estoque', 'descricao', 'lancamento','peso', 'data_de_validade', 'cor', 'categoria']
    #colunas q da pra editar ^^^
    list_display_links = ['id', 'nome']
    list_filter = ['descricao']
    search_fields = ['nome']
    filter_horizontal = ['fornecedor']
# class FornecedorAdmin(admin.ModelAdmin):
#     list_display = ['nome', 'telefone', 'cidade']
#     list_display = ['nome', 'telefone']
#     list_filter = ['nome']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(Fornecedor)