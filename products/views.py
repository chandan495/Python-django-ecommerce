#from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from carts.models import Cart

from .models import Product

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.object.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.object.all().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.object.ProductFeaturedDetailView()



class ProductListView(ListView):
   # queryset = Product.object.all()
    template_name = "products/list.html"

    #def get_context_data(self, *args, **kwargs):
        # context = super(ProductListView, self).get_context_data(*args, **kwargs)
        # print(context)
        # return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.object.all()





def product_list_view(request):
    queryset = Product.object.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)
class ProductDetailSlugView(DetailView):
    queryset = Product.object.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        request = self.request
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Product, slug=slug, active=True)
        # if instance is None:
        #     raise Http404("Product doesn't exist")
        try:
            instance = Product.object.get(slug= slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found any Product")
        except Product.MultipleObjectsReturned:
            qs = Product.object.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("UHHHMMMMMMM")
        return instance

class ProductDetailView(DetailView):
    queryset = Product.object.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.object.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.all()




def product_detail_view(request, pk=None, *args, **kwargs):
    #instance  = Product.objects.get(pk=pk) #id
   # instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('No Product Here')
    #     raise Http404("Product does not exist")
    # except:
    #     print("Huhhhh?")

    qs = Product.object.filter(id=pk)
    if qs.exists() and qs.count==1:
        instance = qs.first()
    else:
        raise Http404("Product does not exist")
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)