from django.shortcuts import render

def PortfolioView(request):
    return render(request, 'Portfolio/Portfolio.html')