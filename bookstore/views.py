from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Books
from django.core import serializers
from django.template import loader 
# Create your views here.

def home(request):
    all_books = Books.objects.all()
    context ={
       "list_books":all_books
    }
    return render(request, 'bookstore/index.html',context)

def search(request):
    if request.method == "POST":
        book_name = request.POST.get('search')
        try:
            all_books = Books.objects.filter(name__icontains = book_name)
            context ={
            "list_books":all_books
            }
            return render(request, 'bookstore/index.html',context)
        except:
            return render(request,'bookstore/index.html',{})
    else:
        return render(request,'bookstore/index.html',{})

 
def del_book(request,pk):
    if request.method == "GET":
        book = Books.objects.get(pk=pk)
        book.delete()
        return JsonResponse({"message":"success"})
    return JsonResponse({"message":"Wrong route"})