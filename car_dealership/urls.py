from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'car_dealership.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'carmanager.views.import_cars', name='home'),
    url(r'^search_form/$', 'carmanager.views.search_form', name='search_form'),
    url(r'^search/$', 'carmanager.views.search', name='search'),
    url(r'^cars/(?P<car_id>\w+)/edit$', 'carmanager.views.edit_cars', name='edit_cars'),
    url(r'^cars/(?P<car_id>\w+)/delete$', 'carmanager.views.delete_cars', name='delete_cars'),
    url(r'^add/$', 'carmanager.views.add_cars', name='add_cars'),
    url(r'^admin/', include(admin.site.urls)),
)
