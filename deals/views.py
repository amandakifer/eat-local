from django.shortcuts import render
from libs.wrapper import Yelp
from deals import forms as deals_forms


def index(request):
    context = {}
    if request.GET:
        form = deals_forms.LocationForm(request.GET)
        if form.is_valid():
            yelp_wrapper = Yelp()
            search_terms = form.cleaned_data['search_terms']
            location = form.cleaned_data['location']
            context['location'] = location
            results = yelp_wrapper.search(search_terms, location, deals_filter=True)
            context['results'] = results
    else:
        form = deals_forms.LocationForm()

    context['form'] = form
    return render(request, 'deals/deals.html', context)

