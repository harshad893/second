from django.shortcuts import render

# Create your views here.
def htmlFile(request):
    return render(request,'hai.html')