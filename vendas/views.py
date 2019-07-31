from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count
from .models import Venda
from .forms import ItemPedidoForm


class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso Negado!')

        return super(DashboardView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        Venda.objects.media()
        data={}
        data['media'] = Venda.objects.media()
        data['media_desc'] = Venda.objects.media_desconto()
        data['min'] =  Venda.objects.mim()
        data['max'] =  Venda.objects.max() 
        data['n_ped'] =  Venda.objects.num_pedidos()
        data['n_ped_nfe'] =  Venda.objects.num_ped_nefe()

        return render(request, 'vendas/dashboard.html', data)

class NovoPedido(View):
    def get(self, request):
        return render(request, 'vendas/novo-pedido.html')
    
    def post(self, request):
        data={}
        data['numero']=request.POST['numero']
        data['desconto']=float(request.POST['numero'])
        data['venda'] = request.POST['venda_id']

        if data['venda']:
            venda=Venda.objects.get(id=data['venda'])
            venda.desconto=data['desconto']
            venda.numero=data['numero']
            venda.save()
        else:
            venda=Venda.objects.create(
                numero=data['numero'], desconto=data['desconto'])
        
        itens=venda.itemdopedido_set.all()
        data['venda_obj']=venda
        data['itens']=itens
        return render(
            request, 'vendas/novo-pedido.html', data)

class NovoItemPedido(View):
    def get(self, request, pk):
        pass
    
    def post(self, request, venda):
        data = {}
        item=ItemDoPedido.objects.create(
            produto_id=request.POST['produto_id'], quantidade=request.POST['quantidade'],
            desconto=request.POST['desconto'], venda_id=venda)

        data['item'] = item
        data['form_item'] = ItemPedidoForm()
        data['numero'] = item.venda.numero
        data['desconto'] = item.venda.desconto
        data['venda'] = item.venda.id
        data['venda_obj'] = item.venda
        data['itens'] = item.venda.itemdopedido_set.all()
        return render(
            request, 'vendas/novo-pedido.html', data)

class ListaVendas(View):
    def get(self, request):
        vendas=Venda.objects.all()
        return render(request, 'vendas/lista-vendas.html', {'vendas': vendas})