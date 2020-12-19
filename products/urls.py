
from django.conf.urls import url

from products.views import (ProductListView,
                            product_list_view,ProductDetailView,product_detail_view,
                            #ProductFeaturedListView,
                            #ProductFeaturedDetailView,
                            ProductDetailSlugView
                           )
from . import views


urlpatterns = [

    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detailpk'),
    #url(r'^$', product_list_view),
]
