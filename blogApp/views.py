from django.shortcuts import render # type: ignore


# Create your views here.
def Starting_page(request):
  return render(request,"blogApp/index.html")

def Posts(request):
   return render(request,"blogApp/all-posts.html")


def Posts_detail(request,slug ):
   return render(request,"blogApp/post-detail.html")


  

