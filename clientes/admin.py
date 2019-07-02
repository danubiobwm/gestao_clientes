from django.contrib import admin
from .actions import nfe_emitida, nfe_nao_emitida
from .models import Person, Documento, Venda, Produto

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados Pessois', {'fields': ( 'doc', 'first_name', 'last_name')}),
        ('Dados Complementares', { 'classes':('collapse',), 
        'fields': ('age', 'salary', 'photo' )
        })
    )
    #fields=('doc', 'first_name', 'last_name', 'age', 'salary', 'bio', 'photo'  )
    list_filter = ('age', 'salary')
    list_display = ('doc', 'first_name', 'last_name', 'age', 'salary', 'bio', 'tem_foto' )
    search_fields=('id', 'first_name')

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'
    tem_foto.shor_description = 'Possui Foto'


class VendaAdmin(admin.ModelAdmin):
    readonly_fields=('valor',)
    list_filter = ('pessoa__doc', 'desconto')
    autocomplete_fields  = ("pessoa", "produtos")
    list_display=('id', 'pessoa', 'get_total', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions=[nfe_emitida, nfe_nao_emitida]
    

    def total(self, obj):
        return obj.get_total()

    total.shor_description='total'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')
    search_fields = ['id', 'descricao']


class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['num_doc']


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
