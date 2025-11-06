from django.shortcuts import render
from .models import bloginfo

# Create your views here.
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        blogObj=bloginfo(title=title, content=content)
        blogObj.save()
    return render(request,'create.html')


def list(request):
    posts = bloginfo.objects.all()
    return render(request,'list.html',{'posts': posts})