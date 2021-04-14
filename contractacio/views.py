from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Contracte

# Create your views here.

def post_list(request):
    contractes = Contracte.objects.all().order_by('termini_presentacio_instancies')
    return render(request, 'contractacio/post_list.html', {'contractes': contractes})


def detall(request, pk):
    contracte = get_object_or_404(Contracte, pk=pk)
    return render(request, 'contractacio/detall.html', {'contracte': contracte})