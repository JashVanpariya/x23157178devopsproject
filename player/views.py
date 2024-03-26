from django.shortcuts import render, redirect
from .models import Player
from .forms import PlayerForm

def players_list(request):
    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'player/list.html', context)

def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('players-list')
    else:
        form = PlayerForm()
    
    context = {
        'form': form,
    }
    return render(request, 'player/create.html', context)

def edit_player(request, player_id):
    player = Player.objects.get(id=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('players-list')
    else:
        form = PlayerForm(instance=player)
    
    context = {
        'player': player,
        'form': form,
    }
    return render(request, 'player/edit.html', context)

def delete_player(request, player_id):
    player = Player.objects.get(id=player_id)
    if request.method == 'POST':
        player.delete()
        return redirect('players-list')
    
    context = {
        'player': player,
    }
    return render(request, 'player/delete.html', context)
