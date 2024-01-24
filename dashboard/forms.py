from django import forms
from dashboard.models import Product, Category, Order





class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['product', 'order_quantity']



class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)



