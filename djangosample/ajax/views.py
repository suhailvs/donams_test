from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import UserDetail,UserDetailForm
def index(request):
    return render(request,"home.html",{'page':'users'})

def ajax_showpage(request):
    curpage=request.GET['page']
    context = {'page':curpage}
    if curpage=='users':
        template='users.html'
        context['users']=UserDetail.objects.all()#['suhail','sumee','vahee']
    elif curpage=='add':
        template = 'add_user.html'
    
    return render(request,template,context)

def ajax_adduser(request):
    if request.method=="POST":
        form = UserDetailForm(request.POST)
        if form.is_valid():
            form.save()
        for key,value in request.POST.items():
            print (key, value) 
    return HttpResponse('hai')

