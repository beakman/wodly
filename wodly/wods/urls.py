# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the WodListView
    url(
        regex=r'^user/(?P<username>[\w.@+-]+)/$',
        view=views.WodListView.as_view(),
        name='list'
    ),

    # URL pattern for the WodDetailView
    url(
        regex=r'^user/(?P<username>[\w.@+-]+)/(?P<pk>\d+)/$',
        view=views.WodDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the WodUpdateView
    url(
        regex=r'^~update/(?P<pk>\d+)/$',
        view=views.WodUpdateView.as_view(),
        name='update'
    ),    

    # URL pattern for the WodCreateView
    url(
        regex=r'^~new/$',
        view=views.WodCreateView.as_view(),
        name='new'
    ),
]
