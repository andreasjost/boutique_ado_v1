from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51GqK4sEZw43pLUwHzccr2jhwn5G2VFvJZDXHZAQO8oZU5DjrDUZhN91xXbK9nG8tvJjTkNaLhj7dbWFKSs2rf8Ju00nA5AugnU',
        'client_secret': 'test client',
    }

    return render(request, template, context)
