from django.contrib import admin
from .models import Person, Documento, Venda, Produto

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados Pessois', {'fields': ( 'doc', 'first_name', 'last_name')}),
        ('Dados Complementares', { 'classes':('collapse',), 
        'fields': ('age', 'salary', 'photo' )
        })
    )
    
    #fields=('doc', 'first_name', 'last_name', 'age', 'salary', 'bio', 'photo'  )
    list_display = ('doc', 'first_name', 'last_name', 'age', 'salary',
     'bio', 'photo' )
    
    list_filter = ('age', 'salary')

class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc', 'desconto')

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto)
