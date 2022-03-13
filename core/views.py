from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def webrtc(request):
    context = {
        'usr': request.GET.get('user', 'NA') 
    }
    return render(request, 'webrtc.html', context)