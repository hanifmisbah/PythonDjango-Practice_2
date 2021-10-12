from django.shortcuts import redirect, render

from . import models
# Create your views here.
def ktgori(req):
    if req.POST:
        models.Kategori.objects.create(
            kate=req.POST['kate']
        )
    makan1 = models.Kategori.objects.all()
    return render(req, 'input_ktgori.html', {
        'data':makan1
    })

def input(req):
    if req.POST:
        models.Makan.objects.create(
            nama=req.POST['nama'],
            ktgori=req.POST['ktgori'],
            harga=req.POST['harga'],
        )
        return redirect('/')
    makan1 = models.Makan.objects.all()
    return render(req, 'input.html', {
        'datamakan': makan1
    })
    