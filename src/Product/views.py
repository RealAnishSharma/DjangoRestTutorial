from django.db import models
from django.shortcuts import render
from .forms import AddProductForm
from .models import Product
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

class ProductListView(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'Product/list.html'
    paginate_by = 3
    

@login_required
def add_product_view(request):    
    alert_message = None
    form = AddProductForm()
    if request.method=='POST':
        form = AddProductForm(request.POST,request.FILES)
        # name = request.POST.get('name')
        # description = request.POST.get('description')
        # image = request.POST.get('image')
        # price = request.POST.get('price')
        # product = Product.objects.create(name=name,description=description,price=price,image=image)
        #product.save()

        if form.is_valid():
            form.save()
            alert_message = "SucessFully Added"

    context ={
        'form':form,
        'alert_message':alert_message,
    }
    return render(request,'Product/add_product.html',context)

class ProductDelete(DeleteView):
    model = Product
    success_url='/products/list'
    #template_name = 'Product/list.html'