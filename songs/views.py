# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Song, Performer
# Create your views here.


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})

def song_detail(request, pk):
    #song_detail = Song.objects.get(pk=pk)
    detail = get_object_or_404(Song, pk=pk)
    return render(request, 'songs/song_detail.html', {'song': detail})

def performer_detail(request, performer_pk):
    performer = get_object_or_404(Performer,song_id=song.pk, pk=performer_pk)
    return render(request, 'songs/performer_detail.html', {'performer': performer})
#    performer = get_object_or_404(Performer, pk=pk)
#    return render(request, 'songs/performer_detail', {'performer': performer})
