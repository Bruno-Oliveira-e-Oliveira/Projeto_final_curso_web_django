from django.contrib import admin
from .models import (Pessoa,
    Marca,
    Veiculo,
    Parametros,
    MovimentoRot,
    Mensalista,
    MovimentoMens
)


class MovimentoRotAdmin(admin.ModelAdmin):
    list_display = (
        'checkin','checkout','valor_hora','pago',
        'horas_total','total','veiculo'
    )

    


class MovimentoMensAdmin(admin.ModelAdmin):
    list_display = ('mensalista','dt_pgto','total')






admin.site.register(Pessoa)
admin.site.register(Mensalista)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(MovimentoRot,MovimentoRotAdmin)
admin.site.register(MovimentoMens,MovimentoMensAdmin)
