from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

from deals import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='deals', permanent=True)),
    url(r'^deals/', include(urls), name='deals'),
]
