from django.contrib import admin
from .models import Person, Documento, Venda, Produto

class PersonAdmin(admin.ModelAdmin):
    fields=('doc', 'first_name', 'last_name', 'age', 'salary',
     'bio', 'photo'  )
    list_display = ('doc', 'first_name', 'last_name', 'age', 'salary',
     'bio', 'photo' )


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
