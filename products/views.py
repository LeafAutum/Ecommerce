from django.views.generic import ListView , DetailView
from django.shortcuts import render , get_object_or_404
from django.http import Http404
from carts.models import Cart
from .models import Product

class ProductFeaturedListView(ListView):
      template_name="products/list.html"

      def get_queryset(self,*args,**kwargs):
          request=self.request
          return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
      queryset=Product.objects.all().featured()
      template_name="products/featured-detail.html"
      # def get_queryset(self,*args,**kwargs):
      #     request=self.request
      #     pk=self.kwargs.get('pk')
      #     return Product.objects.featured()


class ProductListView(ListView):
      queryset=Product.objects.all()
      template_name="products/list.html"

      # def get_context_data(self, *args, **kwargs):
      #     context=super(ProductListView, self).get_context_data(*args, **kwargs)
      #     print(context)
      #     return context
      def get_queryset(self,*args,**kwargs):
          request=self.request
         # print(Product.objects.all())
          return Product.objects.all()


def product_list_view(request):
    queryset=Product.objects.filter()
    #print(queryset)
    context={
          'object_list':queryset
    }
    return render(request,'products/list.html', context)


class ProductDetailSlugView(DetailView):
      queryset=Product.objects.all()
      print(queryset)
      template_name="products/detail.html"

      def get_context_data(self, *args, **kwargs):
          context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
          cart_obj, new_obj = Cart.objects.new_or_get(self.request)
          context['cart']=cart_obj
          print("detailed,", context)
          return context

      def get_object(self, *args, **kwargs):
          request=self.request
          print("kwargs",self.kwargs,args)
          slug=self.kwargs.get('slug')
          print("yyyyyyyyyy",slug)
          #instance=get_object_or_404(Product,slug=slug, active=True)
          try:
              instance=Product.objects.get(slug=slug)
              print(instance)
          except Product.DoesNotExist:
                   raise Http404("not found...")
          except Product.MultipleObjectsReturned:
              qs=Product.objects.filter(slug=slug)
              print(qs)
              instance= qs.first()
          except:
               raise Http404("hummmmmm")
          return instance




class ProductDetailView(DetailView):
      #queryset=Product.objects.all()
      template_name="products/detail.html"

      def get_context_data(self, *args, **kwargs):
          context=super(ProductDetailView, self).get_context_data(*args, **kwargs)
          print(context)
          #context['abc']=123
          return context
      # def get_object(self, *args, **kwargs):
      #     request=self.request
      #     print(kwargs)
      #     pk=self.kwargs.get('pk')
      #     instance=Product.objects.get_by_id(pk)
      #     if instance== None:
      #          raise Http404("product doesnt exist")
      #     return instance
      #
      def get_queryset(self,*args,**kwargs):
          request=self.request
          print("request",request,self.kwargs)
          pk=self.kwargs.get('pk')

          return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None,*args, **kwargs):
     instance=Product.objects.get(pk=pk, featured=True)
     #instance=get_object_or_404(Product,pk=pk)
     #print(args)
     #print(kwargs)
      # try:
      #    instance=Product.objects.get(pk=pk)
      # except Product.DoesNotExist:
      #    print("no found")
      #    raise Http404("product doesnt exist")
      # except:
      #    print('huhs')

      # qs=Product.objects.filter(pk=pk)
      # print(qs.first())
      # if qs.exists() and qs.count()== 1:
      #     instance= qs.first()
      # else:
      #     raise Http404("product doesnt exist")
     instance=Product.objects.get_by_id(pk)
     if instance== None:
          raise Http404("product doesnt exist")
     context={
          'object':instance
      }
     return render(request,'products/detail.html', context)
