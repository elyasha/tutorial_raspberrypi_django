from django.contrib import admin
from raspberryfr.pidata.models import Medida1

@admin.register(Medida1)
class Medida1Admin(admin.ModelAdmin):
    list_display = (
        "tensao_eletrica",
        "creation_date",
        "modification_date"
    )
