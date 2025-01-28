from django.shortcuts import render # type: ignore


# Create your views here.
def Starting_page(request):
  return render(request,"blogApp/index.html")

def Posts(request):
  pass

def Posts_detail(request ):
  pass

