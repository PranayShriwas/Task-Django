from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Product

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        image = request.POST.get('image')
        
        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username is already taken'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email is already taken'})
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        
        Product.objects.create(
            name=product_name,
            category=category,
            price=price,
            description=description,
            quantity=quantity,
            image=image
        )
        
        return redirect('login')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required
def products(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'page_obj': page_obj})
