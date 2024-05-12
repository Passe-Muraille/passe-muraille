from django.contrib import admin
from .models import Enquete, Indice_chiffres, Indice_autre, Indice_chiffres_trouves, Indice_autre_trouves
from .models import Event

class EnqueteAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'ville')
    list_filter    = ('ville',)
    ordering       = ('ville', 'titre')

class Indice_chiffresAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'id')
    ordering       = ('nom',)

class Indice_autreAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'id')
    ordering       = ('nom',)

class Indice_chiffres_trouvesAdmin(admin.ModelAdmin):
    list_display   = ('equipe', 'indice')
    ordering       = ('equipe', 'indice')

class Indice_autre_trouvesAdmin(admin.ModelAdmin):
    list_display   = ('equipe', 'indice')
    ordering       = ('equipe', 'indice')

admin.site.register(Enquete, EnqueteAdmin)
admin.site.register(Indice_chiffres, Indice_chiffresAdmin)
admin.site.register(Indice_autre, Indice_autreAdmin)
admin.site.register(Indice_chiffres_trouves, Indice_chiffres_trouvesAdmin)
admin.site.register(Indice_autre_trouves, Indice_autre_trouvesAdmin)
admin.site.register(Event)