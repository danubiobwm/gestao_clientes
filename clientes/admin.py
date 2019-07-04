#Admin Clientes
from django.contrib import admin
from .models import Person, Documento

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

class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['num_doc']


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)


