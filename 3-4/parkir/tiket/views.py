from django.shortcuts import redirect, render

from . import models
# Create your views here.
def index(req):
    if req.POST:
        models.Ket.objects.create(
            nopol=req.POST['nopol'],
        )
        return redirect('/')
    data = models.Ket.objects.all()
    return render(req, 'tiket/index.html', {
        'data' : data,
    })