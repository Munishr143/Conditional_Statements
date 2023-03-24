from django.shortcuts import render

# Create your views here.

def Conditional(request):
    d={'a':20, 'b':24, 'c':22}
    return render(request, 'conditional_statements.html', context=d)