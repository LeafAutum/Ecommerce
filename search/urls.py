
from django.conf.urls import url

from search.views import (SearchProductView
                           )
from . import views


urlpatterns = [

    url(r'^$', SearchProductView.as_view(), name='query')
    #url(r'^$', product_list_view),
]
