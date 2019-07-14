from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count
from .models import Venda


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

