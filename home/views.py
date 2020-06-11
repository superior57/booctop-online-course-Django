from django.shortcuts import render
from home.models import User, user_activation
import json
import os, sys
import traceback
import uuid
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, login, logout

def home_view(request):
    print("request = ",request.user.id)
    if request.user.id == None:
        return render(request, 'index.html', {})
    else:
        return render(request, 'index-2.html', {})


def signup(request):
    return render(request, 'signup.html', {})    

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
        print ('email ===', email)
        
        lstUsers = User.objects.filter(email=email)
        print ("len(lstUsers) =",len(lstUsers))
        if len(lstUsers) > 0:
            msg = 'already'
        else:
            
            msg = 'success'
            


    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n" + str(sys.exc_type) + ": " + str(sys.exc_info())
    
    #
    to_return = {'msg': msg}
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")

def register_user(request):

    msg = ''
    try:
        firstname = request.POST.get('first_name')
        print ('firstname ===',firstname)
        lastname = request.POST.get('last_name')
        print ('lastname ===', lastname)
        email = request.POST.get('email')
        print ('email ===', email)
        password = request.POST.get('password')
        print ('password ===', password)
        phone_number = request.POST.get('phone_number')
        print ('phone_number ===', phone_number)


        lstUsers = User.objects.filter(email=email)
        print ("len(lstUsers) =",len(lstUsers))
        if len(lstUsers) > 0:
            msg = 'already'
        else:
            objUser = User(email=email, first_name=firstname, last_name=lastname, phone_number=phone_number, password=password, is_staff=False,
                           is_active=False, is_superuser=False)
            objUser.set_password(password)
            objUser.save()

            objUA = user_activation()
            objUA.user = objUser
            objUA.code = str(uuid.uuid4())
            objUA.save()
            domain = request.META['HTTP_HOST']
            print ('domain ====',domain)
            print ('objua ====',objUA.code)

            msg = 'success'
            sendConfirmationMail(objUA, domain)


    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n" + str(sys.exc_type) + ": " + str(sys.exc_info())
        print ("Register msg = ",msg)
    #
    to_return = {'msg': msg}
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")




def sendConfirmationMail(objUA, domain):

    try:
        link = 'http://' + domain + '/activation?code=' + objUA.code
        print ('link-----',link)
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
        print ('error-----')
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n" + ": " + str(sys.exc_info())
        msg = tbinfo + "\n" + ": " + str(sys.exc_info())
        print(msg)

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
        print('email ===', email)
        password = request.POST.get('password')
        print('password ===', password)
        objU = authenticate(email=email, password=password)
        print(objU)
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

def logout_(request):
    logout(request)
    return HttpResponseRedirect('/')
        