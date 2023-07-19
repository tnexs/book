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
    return render(request, 'bookstore/book.html',context)

def search(request):
    if request.method == "POST":
        book_name = request.POST.get('search')
        try:
            all_books = Books.objects.filter(name__icontains = book_name)
            context ={
            "list_books":all_books
            }
            return render(request, 'bookstore/book.html',context)
        except:
            return render(request,'bookstore/book.html',{})
    else:
        return render(request,'bookstore/book.html',{})

 
def delete(request,id):
    if request.method == "GET":
        book = Books.objects.get(pk=id)
        book.delete()
        return JsonResponse({"message":"success"})
    return JsonResponse({"message":"Wrong route"})