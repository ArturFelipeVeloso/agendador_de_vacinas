from django.contrib import admin
from .models import Agendamento

@admin.register(Agendamento)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'vacina', 'local_vacina', 'data_vacina', 'hora_vacina')