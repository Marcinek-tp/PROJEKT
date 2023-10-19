from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')  #zamiast return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def instrukcje(request):
    return render(request, 'instrukcje.html')

def opismMedica(request):
    return render(request, 'opismMedica.html')

def kursy(request):
    return render(request, 'kursy.html')