from django.shortcuts import render

from libs.wrapper import Yelp


def index(request):
    yelp = Yelp()
    context = {
        # TODO add UI that lets user enter search term and location
        'deals': yelp.search('steak', 'Playa Vista', True),
    }
    return render(request, 'index.html', context)
