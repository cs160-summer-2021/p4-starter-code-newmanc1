# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def small(request):
    return render(request, 'draw/small.html')

def big(request):
    return render(request, 'draw/big.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })
