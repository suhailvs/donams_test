=====================================
Jquery load a page to div from Django 
=====================================

Jquery Load a page from Django views

Frontend
========

`home.html`::

    <div id="ajaxBox"></div>
    $( document ).ready(function() {
      var url_showpage= "{% url 'ajax_showpage' %}?page="
      $('#ajaxBox').load(url_showpage+'{{page}}');
    });

Backend
=======

`views.py`::

    def ajax_showpage(request):
      curpage=request.GET['page']
      context = {'page':curpage}
      if curpage=='users':
        template='users.html'
        context['users']=UserDetail.objects.all()#['suhail','sumee','vahee']
      elif curpage=='add':
        template = 'add_user.html'

      return render(request,template,context)

`urls.py`::

    path('ajx/', views.ajax_showpage, name='ajax_showpage'),
