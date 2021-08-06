from django.contrib import admin
from .models import Agendamento

@admin.register(Agendamento)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'vacina', 'local_primeira_vacina', 'data_primeira_vacina', 'hora_primeira_vacina', 'local_segunda_vacina', 'data_segunda_vacina', 'hora_segunda_vacina')