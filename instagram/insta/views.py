from django.shortcuts import render
from insta.models import Feed
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/admin')
def create(request):
    if request.method=="POST":
        c=request.POST.get('cap')
        f=request.FILES['img']
        u=request.user
        obj=Feed(person=u,cap=c,pic=f)
        obj.save()
    return render(request,'create.html')


def home(request):
    objs=Feed.objects.all()
    if request.method=="POST":
        a=request.POST.get('srch')
        res=Feed.objects.filter(cap__icontains=a)
        return render(request,'home.html',{'posts':res})
    return render(request,'home.html',{'posts':objs})



