from django.shortcuts import redirect, render

from . import models
# Create your views here.

def index(req):
    if req.POST:
        models.Minum.objects.create(
            item=req.POST['item'],
            jenis=req.POST['jenis'],
            harga=req.POST['harga'],
        )
        return redirect('/')
    minum = models.Minum.objects.all()
    return render(req, 'index.html', {
        'data' : minum,
    })