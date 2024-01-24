from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Order
from dashboard.forms import ProductForm, CategoryForm,  OrderForm
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.views import generic
from django.contrib import messages



@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    workers_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    category_count = Category.objects.all().count()
    order_count = Order.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        "orders": orders,
        "form": form,
        "products": products,
        "workers_count": workers_count,
        "product_count": product_count,
        "order_count": order_count,
        "category_count": category_count,
    }
    return render(request, 'dashboard/index.html', context)


@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    product_count = Product.objects.all().count()
    order_count = Order.objects.all().count()
    category_count = Category.objects.all().count()
    context = {
        "workers": workers,
        "workers_count": workers_count,
        "product_count": product_count,
        "order_count": order_count,
        "category_count": category_count,
    }
    return render(request, 'dashboard/staff.html', context)


@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        "workers": workers
    }
    return render(request, 'dashboard/staff_detail.html', context)




@login_required
def product(request):
    items = Product.objects.all()
    product_count = items.count()
    workers_count = User.objects.all().count()
    order_count = Order.objects.all().count()
    category_count = Category.objects.all().count()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')

            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        "items": items,
        "form_product": form,
        "product_count": product_count,
        "workers_count": workers_count,
        "order_count": order_count,
        "category_count": category_count,
    }
    return render(request, 'dashboard/product.html', context)


@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')


@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        "form": form
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required
def order(request):
    orders = Order.objects.all()
    order_count = orders.count()
    workers_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    category_count = Category.objects.all().count()
    context = {
        "orders": orders,
        "order_count": order_count,
        "workers_count": workers_count,
        "product_count": product_count,
        "category_count": category_count,
    }
    return render(request, 'dashboard/order.html', context)


@login_required
def category(request):
    categories = Category.objects.all()
    category_count = categories.count()
    workers_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    order_count = Order.objects.all().count()
    error = ""
    if request.method == 'POST':
        name = request.POST["name"]
        try:
            Category.objects.create(name=name,)
            error = "no"
        except:
            error = "yes"
    context = {
        "error": error,
        "categories": categories,
        "category_count": category_count,
        "workers_count": workers_count,
        "product_count": product_count,
        "order_count": order_count,
    }
    return render(request, 'dashboard/categories.html', context)


@login_required()
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('category-page')






# @login_required()
# def update_category(request, ppk):
#     items = Category.objects.get(id=ppk)
#     if request.method == 'POST':
#         forms = CategoryUpdateForm(request.POST, instance=items)
#         if forms.is_valid():
#             forms.save()
#             return redirect('category-page')
#     else:
#         forms = CategoryUpdateForm(instance=items)
#     context = {
#         "forms": forms
#     }
#     return render(request, 'dashboard/category_update.html', context)

# @login_required()
# def update_category(request, pk):
#
#     category = Category.objects.get(id=pk)
#     if request.method == 'POST':
#         name = request.POST['name']
#         Category.objects.update(name=name, instance=category)
#         return redirect('category-update')
#     context = {
#         "category": category
#
#     }
#     return render(request, 'dashboard/categories.html', context)

# @login_required
# def category(request):
#     categories = Category.objects.all()
#     context = {
#         "categories": categories
#     }
#     return render(request, 'dashboard/categories.html', context)
#
#
# @login_required
# def category_add(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('category-page')
#         else:
#             form = CategoryForm()
#     context = {
#         "form": form
#     }
#     return render(request, 'dashboard/categories.html', context)

# @login_required
# def category(request):
#     category = Category.objects.all()
#
#     if request.method == 'POST':
#         form_category = CategoryForm(request.POST)
#         if form_category.is_valid():
#             form_category.save()
#             return redirect('category-page')
#     else:
#         form_category = ProductForm()
#     context = {
#         "categories": category,
#         "form_category": form_category
#     }
#     return render(request, 'dashboard/categories.html', context)



# def category(request):
#     categories = Category.objects.all()
#
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('category-page')
#     else:
#         form = CategoryForm()
#     context = {
#         "categories": categories,
#         "form_category": form
#     }
#     return render(request, 'dashboard/product.html', context)
