import os, fnmatch

from django.http import HttpResponse
#from django.template import loader # for html
from django.shortcuts import render

from .Forms.formManger import inputForm
# Create your views here.

def loadPagelinks():
    pages = fnmatch.filter(os.listdir('./polls/templates/polls/'), "*.html")
    pages.remove('main.html')

    return pages

def djangoMain(request):
    #main_page = loader.get_template('polls/index.html')
    links = loadPagelinks()
    print(links)
    return render(request, 'polls/main.html', {'links':links})


from polls.models import Userinfo, Userbirth
def djangoInputpage(request):

    formclass = inputForm(request.POST)
    if request.method == "POST":
        print(Userinfo.objects.all())
        
        
        #submit for POST
        if formclass.is_valid():# checking input data in form
            #print("\n\n\n"+ str(formclass['u_name'].data))
            userinfo = Userinfo(u_name=formclass['u_name'].data,
                                u_hobby=formclass['u_hobby'].data)
            userinfo.save()
            
            fk_userbirth = Userbirth(user=userinfo,
                                     u_birth=formclass['u_birth'].data)
            fk_userbirth.save()
    
    return render(request, 'polls/inputPage.html', {'formclass':formclass})

