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
        return redirect('/makanan/')
    makan = models.Makan.objects.all()
    return render(req, 'makan/index.html', {
        'data' : makan,
    })

def hapus(req, id):
    models.Makan.objects.filter(pk=id).delete()
    return redirect('/makanan')

def edit(req, id):
    if req.POST:
        models.Makan.objects.filter(pk=id).update(
            item=req.POST['item'],
            jenis=req.POST['jenis'],
            harga=req.POST['harga'],
        )
        return redirect('/minuman/')
    
    makan = models.Makan.objects.all()
    return render(req, 'makan/edit.html', {
        'data' : makan,
    })