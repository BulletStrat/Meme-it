from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Meme
from .forms import MemeForm


def home(request):
    queryset = Meme.objects.all() # ordered by creation_date
    paginator = Paginator(queryset, 6)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var
    }
    return render(request, "index.html", context)


def upload_meme(request):
    form = MemeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Successfully Created")
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

def delete_meme(request, id=None):
    instance = get_object_or_404(Meme, id=id)
    if not request.user == instance.user or not request.user.is_superuser:
        raise Http404
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("memes:home")
