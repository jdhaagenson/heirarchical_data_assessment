from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import File


# Create your views here.
def show_files(request):
    files = File.objects.all()
    return render(request, "files.html", {'files': files})

