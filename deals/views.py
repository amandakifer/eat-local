from urllib import urlencode

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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
            context['url'] = '?%s' % urlencode({'search_terms': search_terms, 'location': location})
            results = yelp_wrapper.search(search_terms, location, deals_filter=True)

            paginator = Paginator(results.get('businesses'), 5)
            page = request.GET.get('page')
            try:
                businesses = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                businesses = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                businesses = paginator.page(paginator.num_pages)

            context['businesses'] = businesses
    else:
        form = deals_forms.LocationForm()

    context['form'] = form
    return render(request, 'deals/deals.html', context)

