from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.db.models import Q
from rest_framework import generics
from .models import book,Author,Genre
from .serializers.serializer import BookSerializer,AuthorSerializer,GenreSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.conf import settings
from django.template import loader
from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import AddBook
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


#Responsible for GET and POST REST API Request 
class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):

        queryset = book.objects.all()
        
        return queryset

#Responsible for PUT,PATCH and DELETE REST API Request
class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = book.objects.all()

class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    def get_queryset(self):

        queryset = Author.objects.all()
        
        return queryset

#Responsible for PUT,PATCH and DELETE REST API Request
class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class GenreList(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    def get_queryset(self):

        queryset = Genre.objects.all()
        
        return queryset

#Responsible for PUT,PATCH and DELETE REST API Request
class GenreDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset =  Genre.objects.all()


def testing(request):
    books = book.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'books': books,
    }
    data = {"content": "Gfg is the best"}
    return render(request, "index.html", context)
    
    # no results found for this club id!




# def your_view(request):
#     queryset = book.objects.all()
#     paginator = Paginator(queryset, 10)  # Show 10 items per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     # return render(request, 'index.html', {'page_obj': page_obj})
#     context = {
#         'data': queryset
#     }
#     return render(request, 'dashboard/index.html', context)

# def home(request):
#  return render(request, "home.html", {})
@login_required
def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(title__icontains=q) | Q(author__icontains=q)| Q(genre__icontains=q))
        data = book.objects.filter(multiple_q)
    else:
        data = book.objects.all()
    context = {
        'data': data
    }
    return render(request, 'dashboard/index.html', context)

{csrf_exempt}
def createBooks(request):
    form = AddBook()
    context = {"form":form}
    if request.method == 'POST':
        print('Printing ',request.POST)
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'forms/create.html', context)

{csrf_exempt}
def updateBooks(request,pk):
    bookvar =  book.objects.get(id=pk)
    

    form = AddBook(request.POST,instance=bookvar)
    context = {"form":form}
    if request.method == 'POST':
        print('Printing ',request.POST)
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'forms/create.html', context)

def deleteBooks(request,pk):
    bookvar =  book.objects.get(id=pk)
    # form = AddBook(request.POST,instance=bookvar)
    context = {"form":bookvar}
    if request.method == 'POST':
        bookvar.delete()
        return redirect('/')
    return render(request, 'forms/delete.html', context)

def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("templates/base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})




