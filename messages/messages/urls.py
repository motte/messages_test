from django.conf.urls import patterns, include, url

# App View Imports
from message_app.views import PostMessageView, StatMessageView

# Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(regex=r'^$',
        view=PostMessageView.as_view(),
        name='index'
    ),

    url(regex=r'^stat/get$',
        view=StatMessageView.as_view(),
        name='state_messages'
    ),

    url(r'^admin/', include(admin.site.urls)),
)
