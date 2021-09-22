from django.contrib import admin
from .models import Etudiant, EtudiantPayment, Pavillon, Chambre, Codification

admin.site.register(Etudiant)
admin.site.register(EtudiantPayment)
admin.site.register(Pavillon)
admin.site.register(Chambre)
admin.site.register(Codification)
