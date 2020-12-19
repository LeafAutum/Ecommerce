"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url , include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from products.views import (ProductListView, product_list_view,ProductDetailView,product_detail_view,
#                             ProductFeaturedListView,
#                             ProductFeaturedDetailView,
#                             ProductDetailSlugView
#                            )
from . import views
from carts.views import cart_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page,name='home'),
    #path('wt/', views.mee),
    path('login/', views.login_page,name='login'),
    path('register/', views.register_page,name='register'),
    #url(r'cart/$', cart_home,name='cart'),
    url(r'^cart/', include(("carts.urls",'cart'),namespace='cart')),
    url(r'^products/', include(("products.urls",'products'),namespace='products')),
    url(r'^search/',include(("search.urls","search"),namespace='search')),
    # url(r'^products/$', ProductListView.as_view()),
    # path('products-fbv/', product_list_view),
    # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    #url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedListView.as_view()),
    # url(r'^featured/$', ProductFeaturedDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns=urlpatterns+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
