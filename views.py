from django.shortcuts import render

# Create your views here.

def index(request):

    return  render(request,'index.html')
def watch(request):
    return render(request,'watch.html')
