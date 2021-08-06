from django.shortcuts import render, redirect
from .models import Agendamento
from .forms import AgendamentoForm

# Create your views here.
def agendamento(request):  
    agendamentos = Agendamento.objects.all()
    
    if request.method=='POST':
        form = AgendamentoForm(request.POST)
            
        if form.is_valid():
            form.save()
            return redirect('mensagem')          
    else:
        form = AgendamentoForm()
    
        dados = {
            "form": form,
        }
        
        return render(request, "site.html", dados)
    
def mensagem(request):
    return render(request, "mensagem.html")