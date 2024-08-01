from django.contrib import admin
from .models import Enquete, Indice_chiffres, Indice_autre, Indice_chiffres_trouves, Indice_autre_trouves, Indices_trouves, Messagerie
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

"""class Indice_chiffres_trouvesAdmin(admin.ModelAdmin):
    list_display   = ('equipe', 'indice', 'date_decouverte')
    ordering       = ('equipe', 'indice', 'date_decouverte')
    list_filter    = ('equipe', 'indice')

class Indice_autre_trouvesAdmin(admin.ModelAdmin):
    list_display   = ('equipe', 'indice', 'date_decouverte')
    ordering       = ('equipe', 'indice', 'date_decouverte')
    list_filter    = ('equipe', 'indice')"""

class Indice_trouvesAdmin(admin.ModelAdmin):
    list_display   = ('equipe', 'nom', 'date_decouverte')
    ordering       = ('equipe', 'nom', 'date_decouverte')
    list_filter    = ('equipe', 'nom')

class MessagerieAdmin(admin.ModelAdmin):
    list_display   = ('equipe', 'message', 'date_envoie', )
    ordering       = ('date_envoie',)
    list_filter    = ('equipe',)

admin.site.register(Enquete, EnqueteAdmin)
admin.site.register(Indice_chiffres, Indice_chiffresAdmin)
admin.site.register(Indice_autre, Indice_autreAdmin)
#admin.site.register(Indice_chiffres_trouves, Indice_chiffres_trouvesAdmin)
#admin.site.register(Indice_autre_trouves, Indice_autre_trouvesAdmin)
admin.site.register(Indices_trouves, Indice_trouvesAdmin)
admin.site.register(Messagerie, MessagerieAdmin)
admin.site.register(Event)
