from django.conf.urls import include, url
from django.contrib import admin
from deals import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
        url(r'^deals/', include(urls), name='deals'),
]
