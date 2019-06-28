from django.shortcuts import render
from lojinha.forms import PedidoForm
# Create your views here.
# na views é definido como eu vou trar as minhas requisições.

def mostrar_index(request):
    formulario = PedidoForm(request.POST or None)
    msg =''
    if formulario.is_valid():
        formulario.save()
        formulario = PedidoForm()
        msg = 'Pedido realizado com sucesso'
    contexto = {
        'form' : formulario,
        'msg' : msg
    }
    return render(request, 'index.html', contexto)

