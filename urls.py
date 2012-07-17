from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DJStatusForMe.views.home', name='home'),
    # url(r'^DJStatusForMe/', include('DJStatusForMe.foo.urls')),
      url(r'^mentalnote/$, 'mentalnote.views.index'),
      url(r'^mentalnote/?P<note_id>\d+)/$', mentalnote.views.detail'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
