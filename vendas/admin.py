#Admin Vendas
from django.contrib import admin
from .actions import nfe_emitida, nfe_nao_emitida
from .models import ItensDoPedido, Venda

class VendaAdmin(admin.ModelAdmin):
    readonly_fields=('valor',)
    list_filter = ('pessoa__doc', 'desconto')
    list_display=('id', 'pessoa', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions=[nfe_emitida, nfe_nao_emitida]
    

    def total(self, obj):
        return obj.get_total()

    total.shor_description='total'


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensDoPedido)