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
        return redirect('/minuman/')
    minum = models.Minum.objects.all()
    return render(req, 'minum/index.html', {
        'data' : minum,
    })

def hapus(id):
    models.Minum.objects.filter(pk=id).delete()
    return redirect('/')

def edit(req, id):
    if req.POST:
        models.Minum.objects.filter(pk=id).update(
            item=req.POST['item'],
            jenis=req.POST['jenis'],
            harga=req.POST['harga'],
        )
        return redirect('/minuman/')
    
    minum = models.Minum.objects.all()
    return render(req, 'minum/edit.html', {
        'data' : minum,
    })