from django.shortcuts import render

# Create your views here.
def door1(request):
    return render(request, 'choice/door1.html')

def door2(request):
    return render(request, 'choice/door2.html')

def door3(request):
    return render(request, 'choice/door3.html')

def door11(request):
    return render(request, 'choice/door11.html')

def door13(request):
    return render(request, 'choice/door13.html')

def door22(request):
    return render(request, 'choice/door22.html')

def door23(request):
    return render(request, 'choice/door23.html')

def door32(request):
    return render(request, 'choice/door32.html')

def door33(request):
    return render(request, 'choice/door33.html')