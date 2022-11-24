from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_barang_mywatchlist = MyWatchList.objects.all()
    
    sudah = 0;
    belum = 0;
    for key in data_barang_mywatchlist:
        if key == "fields":
            for x in key:
                if (key == "watched") & (key[x] == True):
                    sudah += 1
                else:
                    belum += 1
    
    if sudah >= belum:
        pesan = 'Selamat, kamu sudah banyak menonton!'
    else:
        pesan = 'Wah, kamu masih sedikit menonton!'

    context = {
        'list_barang': data_barang_mywatchlist,
        'nama': 'Alia Widyanita Puspaningrum',
        'npm': '2106751625',
        'pesan': pesan,
    }
    return render(request, "mywatchlist.html", context)

def show_xml (request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json (request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")