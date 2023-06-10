from django.shortcuts import render

# Create your views here.

def home(request):
   return render(request, 'pages/home.html')

def   categories(request):
      return render(request, 'pages/categories.html')



