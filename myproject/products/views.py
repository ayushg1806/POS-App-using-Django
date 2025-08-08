from django.shortcuts import render, redirect
from products.models import Product, Customer

def home(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    return render(request, 'home.html', {
        'data': products,
        'customer_data': customers,
    })


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('prod_name', '').strip()
        qty = request.POST.get('quantity', '').strip()
        price = request.POST.get('price', '').strip()
        discount = request.POST.get('discount', '').strip()

        if name and qty and price:
            Product.objects.create(
                prod_name=name,
                quantity=int(qty),
                price=float(price),
                discount=float(discount) if discount else 0
            )
    return redirect('home')

def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()

        if name and mobile:
            Customer.objects.create(
                name=name,
                mobile=mobile,
                email=email,
                address=address
            )
    return redirect('home')

def remove_product(request, id):
    Product.objects.get(id=id).delete()
    return redirect('home')

def remove_customer(request, id):
    Customer.objects.get(id=id).delete()
    return redirect('home')

def invoice_view(request):
    customer = Customer.objects.last()  # Get the latest customer added
    products = Product.objects.all()

    total_amount = 0
    for product in products:
        total_amount += product.quantity * product.price * (1 - product.discount / 100)

    return render(request, 'invoice.html', {
        'customer': customer,
        'products': products,
        'total': total_amount
    })