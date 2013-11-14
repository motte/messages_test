from django.conf.urls import patterns, include, url

# App View Imports
from message_app.views import StateMessageView

# Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'messages.views.index', name='index'),

    url(regex=r'^(?P<state>)/get$',
        view=StateMessageView.as_view(),
        name='state_messages'
    ),

    url(r'^admin/', include(admin.site.urls)),
)
