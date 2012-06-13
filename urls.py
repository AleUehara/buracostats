from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buracostats.views.home', name='home'),
    # url(r'^buracostats/', include('buracostats.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    (r'^$'                     , 'information.views.index'),
    (r'^player/$'              , 'information.views.player'),
    (r'^player/add$'           , 'information.views.addplayer'),
    (r'^player/delete/(\d+)$'  , 'information.views.deleteplayer'),
    (r'^gametype/$'            , 'information.views.gametype'),
    (r'^gametype/add$'         , 'information.views.addgametype'),
    (r'^gametype/delete/(\d+)$', 'information.views.deletegametype'),
    (r'^winnerpoints/$'            , 'information.views.winnerpoints'),
    (r'^winnerpoints/add$'         , 'information.views.addwinnerpoints'),
    (r'^winnerpoints/delete/(\d+)$', 'information.views.deletewinnerpoints'),

    (r'^tournament/$'            , 'game.views.tournament'),
    (r'^tournament/add$'         , 'game.views.addtournament'),
    (r'^tournament/delete/(\d+)$', 'game.views.deletetournament'),
    (r'^tournament/view/(\d+)$'  , 'game.views.viewtournament'),
)
