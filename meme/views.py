from django.shortcuts import render, get_object_or_404
from .models import Meme
from .forms import MemeForm


def home(request):
    queryset = Meme.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, "index.html", context)


def upload_meme(request):
    form = MemeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
    }
    return render(request, "upload_form.html", context)

def meme_detail(request, id=None):
    instance = get_object_or_404(Meme, id=id)
    context = {
        "memepost": instance.post,
        "instance": instance
    }
    return render(request, "details.html", context)

def meme_list(request):  #list items not showing
    queryset = Meme.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, "index.html", context)
