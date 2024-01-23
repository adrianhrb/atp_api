from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import FileLoaderForm
from .utils import assign_winners_and_losers, load_database_data


@staff_member_required
def load_data(request):
    if request.method == 'POST':
        form = FileLoaderForm(files=request.FILES)
        if form.is_valid():
            player_file = request.FILES['players']
            match_file = request.FILES['match']
            stats_file = request.FILES['stats']
            load_database_data(player_file, 'P')
            load_database_data(match_file)
            assign_winners_and_losers(stats_file)
            return HttpResponse(status=200)
    else:
        form = FileLoaderForm()
    return render(request, 'loader/load.html', {'form': form})
