from django.shortcuts import render

from . import models
# Create your views here.
def index(req):
    makan1 = models.Makan.objects.all()
    return render(req, 'index.html', {
        'data':makan1
    })