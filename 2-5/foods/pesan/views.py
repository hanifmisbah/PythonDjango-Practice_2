from django.shortcuts import render

from makanan import models as models_makanan
from minuman import models as models_minuman
# Create your views here.
def index(req):
    makan = models_makanan.Makan.objects.all()
    minum = models_minuman.Minum.objects.all()
    return render(req, 'index.html', {
        'data' : makan,
        'data2' : minum,
    })