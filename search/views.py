from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Create your views here.
class SearchProductView(ListView):
      queryset=Product.objects.all()
      template_name="search/view.html"


      def get_queryset(self,*args,**kwargs):
          request=self.request
          print(request.GET)
          query=request.GET.get('q',None)
         # print(Product.objects.all())
         # return Product.objects.all()
          if query is not None:
            # lookups= Q(title__icontains=query) | Q(description__icontains=query)
             return Product.objects.search(query)
          return Product.objects.all()
