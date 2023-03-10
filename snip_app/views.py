from django.contrib.auth.decorators import login_required
from django.shortcuts import (HttpResponse, HttpResponseRedirect, redirect,
                              render)
from feed.models import Post

from .forms import searchForm, snipForm
from .models import Snip


@login_required
def show_snip(request,link_c):
    snips=Snip.objects.order_by('-updated_at')[:10]
    snip=Snip.objects.get(link_code=link_c)
    searchform=searchForm()
    if request.method=="POST":
        try:
            searchform=searchForm(request.POST)
            x = request.POST['search']
            return HttpResponseRedirect("/search/"+x) 
        except ValueError:
            pass
    return render(request, "detail.html", {'searchform':searchform,'snip': snip,'snips':snips})

def all(request):
    snips = Post.objects.all()
    searchform=searchForm()
    if request.method=="POST":
        try:
            searchform=searchForm(request.POST)
            x = request.POST['search']
            return HttpResponseRedirect("/search/"+x) 
        except ValueError:
            pass
    return render(request, 'all.html', {'searchform':searchform,'snips': snips})

@login_required
def index(request):
    snips=Post.objects.order_by('-updated_at')[:8]
    form=snipForm(initial={'author':request.user})
    if request.method=="POST":
        try:
            print(request.POST)
            form=snipForm(request.POST)
            form.save()
            return HttpResponseRedirect("/") 
        except ValueError:
            pass
    searchform=searchForm()
    if request.method=="POST":
        try:
            searchform=searchForm(request.POST)
            x = request.POST.get('search', '')
            return HttpResponseRedirect("/search_posts/?p="+x) 
        except ValueError:
            pass

    return render(request, "index.html", {'searchform':searchform,'form':form, 'snips':snips})

def search(request, link_c):
    snips= Snip.objects.filter(link_code=link_c)
    form=searchForm()
    if request.method=="POST":
        try:
            form=searchForm(request.POST)
            x = request.POST['search']
            return HttpResponseRedirect("/search/"+x) 
        except ValueError:
            pass
    return render(request, "all.html", {'searchform':form,'snips':snips})

@login_required
def delete_snippet(request,snippet_id):
    del_obj=Snip.objects.get(link_code=snippet_id)
    del_obj.delete()
    return HttpResponseRedirect('/all/')

