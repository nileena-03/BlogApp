from django.shortcuts import render,redirect
from .models import bloginfo
from .forms import BlogForm

# Create your views here.
# def create(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         blogObj=bloginfo(title=title, content=content)
#         blogObj.save()
#     return render(request,'create.html')


def list(request):
    posts = bloginfo.objects.all()
    return render(request,'list.html',{'posts': posts})

def create(request):
    if request.method == 'POST' :
        frm = BlogForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('list')

    else:
        frm = BlogForm()
    return render(request,'create.html',{'frm':frm})

def delete(request, id):
    instance = bloginfo.objects.get(id=id)
    instance.delete()
    blogs_set=bloginfo.objects.all()
    return render (request, 'list.html', {'posts':blogs_set})

def edit(request,id):
    instanceToBeEdted = bloginfo.objects.get(id=id)
    if request.method == 'POST':
        frm = BlogForm(request.POST,instance=instanceToBeEdted)
        if frm.is_valid():
            frm.save()
            return redirect('list')

    else:
        frm = BlogForm(instance=instanceToBeEdted)
    return render(request, 'create.html', {'frm':frm})