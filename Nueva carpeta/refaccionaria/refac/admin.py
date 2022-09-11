from django.contrib import admin
from .models import Agenda, Refaccion, Ticket
# Register your models here.

admin.site.site_header = "Refaccionaria Raya"
admin.site.site_title = "Refacciones Raya"
admin.site.index_title = "Bienvenido a la centro de administración de refacciones"



admin.site.register(Agenda)
admin.site.register(Ticket)


@admin.register(Refaccion)
class RefacAdmin(admin.ModelAdmin):
    list_display = ('nombre','modelo','precio','cantidad')