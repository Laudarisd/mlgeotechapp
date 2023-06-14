from django.shortcuts import render, redirect


# Create your views here.

def navBar(request):
    return render(request, 'nav.html')
def homeView(request):
    return render(request, 'main_view.html')
