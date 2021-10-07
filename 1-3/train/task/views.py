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