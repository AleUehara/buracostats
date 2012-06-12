from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buracostats.views.home', name='home'),
    # url(r'^buracostats/', include('buracostats.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$',      'information.views.index'),
    (r'^gametype/$', 'information.views.gametype'),
    (r'^player/$', 'information.views.player'),
    (r'^gametype/add$', 'information.views.addgametype'),
    (r'^player/add$', 'information.views.addplayer'),
)
