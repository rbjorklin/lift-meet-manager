from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lift_meet_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^lift_tables/', include('lift_tables.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
