import os
from django.conf.urls import patterns, include, url
from starter.views import MyFormView, MyListView, MyUpdateView, MyDetailView
from django.views.generic import TemplateView
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^main-page/$', TemplateView.as_view(template_name="main_page.html")),
    url(r'^admin/', include(admin.site.urls)),
)

# model form tests
urlpatterns += patterns(
    (r'^entry-form/$', MyFormView.as_view()),
    (r'^list-forms/$', MyListView.as_view()),
    url(r'^(?P<pk>\d+)/update/$', MyUpdateView.as_view(), name="update_form"),
    url(r'^(?P<pk>\d+)/$', MyDetailView.as_view(), name="detail_view"),
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
    
