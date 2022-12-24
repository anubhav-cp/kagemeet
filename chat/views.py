from django.shortcuts import render
from .models import chatRoom



def index(request):
    rooms = chatRoom.objects.all()
    context = {'rooms': rooms}
    return render(request, 'index.html', context)


def room(request, room_name): 

    context = {'room_name': room_name}
    return render(request, 'chat_room.html', context)
