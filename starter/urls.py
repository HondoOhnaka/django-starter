import os
from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from starter.models import Starter
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url="main/"), name="root_url"),
    (r'^main/$', 'starter.views.main_page'),
    url(r'^admin/', include(admin.site.urls)),
)

# model form tests
urlpatterns += patterns('',
    url(r'^starter/$', ListView.as_view(model=Starter), name="list_page"),
    url(r'^starter/create/$', CreateView.as_view(
            model=Starter,
            success_url=reverse_lazy('list_page')), 
        name="create_page"),
    url(r'^starter/(?P<pk>\d+)/update/$', UpdateView.as_view(
            model=Starter, 
            success_url=reverse_lazy('list_page')),
        name="update_page"),
    url(r'^starter/(?P<pk>\d+)/delete/$', DeleteView.as_view(
            model=Starter, 
            success_url = reverse_lazy('list_page'),
            template_name_suffix="_confirm_delete"),
        name="delete_page"),
    url(r'^starter/(?P<pk>\d+)/$', DetailView.as_view(model=Starter), name="detail_page"),
    )

###################################
## development and test settings ##
###################################

if settings.DEBUG:
    #development site property directories
    
    static_dir = os.path.join(
        os.path.dirname(__file__), '../static'
    )
    
    media_dir = os.path.join(
        os.path.dirname(__file__), '../media'
    )   
    
    urlpatterns += patterns('',
    
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': static_dir }),
    
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': media_dir }),
    )
    
