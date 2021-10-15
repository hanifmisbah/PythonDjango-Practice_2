from django.shortcuts import redirect, render

from . import models
# Create your views here.

def index(req):
    if req.POST:
        models.Makan.objects.create(
            item=req.POST['item'],
            jenis=req.POST['jenis'],
            harga=req.POST['harga'],
        )
        return redirect('/')
    makan = models.Makan.objects.all()
    return render(req, 'makan/index.html', {
        'datamakan' : makan,
    })