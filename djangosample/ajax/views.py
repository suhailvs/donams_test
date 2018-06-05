from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,"home.html",{'page':'users'})

def ajax_showpage(request):
    curpage=request.GET['page']
    context = {'page':curpage}
    if curpage=='users':
        #nts=Notes.objects.filter(user=request.user).order_by('-created')
        template='users.html'
        context['users']=['suhail','sumee','vahee']
    elif curpage=='add':
        template = 'add_user.html'
    
    return render(request,template,context)

def ajax_adduser(request):
    if request.method=="POST":
        for key,value in request.POST.items():
            print (key, value) 
    return HttpResponse('hai')

