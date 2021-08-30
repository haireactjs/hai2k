from django.shortcuts import render
from django.views import View
from .forms import ProductForm
from django.http import HttpResponse
# Create your views here.
class ProductView(View):
    def post(self, request):
        g = ProductForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('lưu thành công')
        else:
            return HttpResponse('không thành công')

    def get(self, request):
        a = ProductForm
        return render(request, 'product.html', {'f': a})
