from django.shortcuts import redirect, render

from . import models
# Create your views here.
def index(req):
    if req.POST:
        models.Task.objects.create(item=req.POST['item'])
        return redirect('/')

    tasks = models.Task.objects.all()
    return render(req, 'home/index.html', {
        'data': tasks,
    })

def detail(req, id):
    detail = models.Task.objects.filter(pk=id).first()
    return render(req, 'home/detail.html', {
        'data': detail,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/')