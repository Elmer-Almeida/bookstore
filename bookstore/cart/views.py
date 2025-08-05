from django.views.generic import View
from django.shortcuts import render


class CartView(View):
    template_name = 'cart/cart.html'

    def get(self, request):
        return render(request, self.template_name)
