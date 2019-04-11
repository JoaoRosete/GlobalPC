from django import template
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status

from .models import Product, Category, SubCategory, Purchase
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import RegistarForm, EditarPerfilForm, InserirProductoForm, InserirCategoriaForm, InserirSubCategoriaForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer, ProductSubCategoryBrandSerializer, SubCategoryProductSerializer, CategorySubCategorySerializer


def loja(request):
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    product = Product.objects.all()
    purchase = Purchase()
    purchase.user = request.GET.get('user')
    purchase.product = request.GET.get('product')
    search_term = ''


    if 'search' in request.GET:
        search_term = request.GET['search']
        product = product.filter(name__icontains=search_term)

    context = {'subcategory': subcategory, 'product': product, 'category': category, 'search_term': search_term, 'purchase': purchase}
    return render(request, 'loja/index.html', context)


def product(request, product_id):
    subcategory_two = SubCategory.objects.all()
    category_two = Category.objects.all()
    product = get_object_or_404(Product, pk=product_id)


    return render(request, 'loja/product-description.html', {'product': product, 'subcategory_two': subcategory_two, 'category_two': category_two})


def subcategory(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, pk=subcategory_id)
    product = Product.objects.all().filter(subcategory_id=subcategory)
    category = Category.objects.all()
    subcategory_two = SubCategory.objects.all()
    category_two = Category.objects.all()
    context = {'subcategory': subcategory, 'product': product, 'category': category, 'subcategory_two': subcategory_two, 'category_two': category_two}
    return render(request, 'loja/subcategory.html', context)


def category_subcategory_allproducts(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    subcategory = SubCategory.objects.all().filter(category_id=category)
    product = Product.objects.all()
    category_two = Category.objects.all()
    subcategory_two = SubCategory.objects.all()
    context = {'category': category, 'subcategory': subcategory, 'product': product, 'category_two': category_two, 'subcategory_two': subcategory_two }
    return render(request, 'loja/category.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/loja/inicio')
    else:
        form = RegistarForm()

    context = {'form': form}
    return render(request, 'loja/register-form.html', context)


def profile(request):
    context = {'user': request.user}
    return render(request, 'loja/profile.html', context)


def editar(request):
    if request.method == 'POST':
        # instance=request.user saber que é o user que queremos
        form = EditarPerfilForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/loja/perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
        context = {'form': form}
        return render(request, 'loja/edit-profile.html', context)


def change_password(request):
    if request.method == 'POST':
        # instance=request.user saber que é o user que queremos
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            # Para nao dar erro ou Anomino User isto serve para dar update ao User
            update_session_auth_hash(request, form.user)
            return redirect('/loja/perfil')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'loja/change-password.html', context)


def insert_product(request):
    form = InserirProductoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()


    context = {'form': form}

    return render(request, 'loja/product-form.html', context)


def insert_category(request):
    form = InserirCategoriaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'loja/category-form.html', context)

def insert_subcategory(request):
    form = InserirSubCategoriaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'loja/subcategory-form.html', context)

def purchases(request):
    purchase = Purchase.objects.all()
    context = {'purchase': purchase}
    return render(request, 'loja/purchases.html', context)


def restframework_links(request):
    return render(request, 'loja/admin-restframework.html')


def insert(request):
    return render(request, 'loja/insert-forms.html')


# Rest Framework
# APIView Product, Category, SubCategory -> List
class ProductList(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class CategoryList(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class SubCategoryList(APIView):
    def get(self, request):
        subcategory = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategory, many=True)
        return Response(serializer.data)


# APIView Product, Category, SubCategory -> Details
class ProductDetails(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSubCategoryBrandSerializer(product, many=False)
        return Response(serializer.data)

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, many=False)
        if product:
            product.delete()
            return Response({})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetails(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySubCategorySerializer(category, many=False)
        return Response(serializer.data)

    def post(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySubCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySubCategorySerializer(category, many=False)
        if category:
            category.delete()
            return Response({})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubCategoryDetails(APIView):
    def get(self, request, pk):
        subcategory = SubCategory.objects.get(pk=pk)
        serializer = SubCategoryProductSerializer(subcategory, many=False)
        return Response(serializer.data)

    def post(self, request, pk):
        subcategory = SubCategory.objects.get(pk=pk)
        serializer = SubCategoryProductSerializer(subcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subcategory = SubCategory.objects.get(pk=pk)
        serializer = SubCategoryProductSerializer(subcategory, many=False)
        if subcategory:
            subcategory.delete()
            return Response({})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)