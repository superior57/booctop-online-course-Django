from django.shortcuts import render
from home.models import User, user_activation
import json
import os, sys
import uuid
from django.http import HttpResponse, HttpResponseRedirect

def home_view(request):
    return render(request, 'index.html', {})


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
            # sendConfirmationMail(objUA, domain)


    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n" + str(sys.exc_type) + ": " + str(sys.exc_info())
        print ("Register msg = ",msg)
    #
    to_return = {'msg': msg}
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")




# def sendConfirmationMail(objUA, domain):
#     try:
#         link = 'http://' + domain + '/activation?code=' + objUA.code
#         txt = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'
#         txt += '<html xmlns="http://www.w3.org/1999/xhtml">'
#         txt += '<head>'
#         txt += '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge">'
#         txt += '<meta name="viewport" content="width=device-width, initial-scale=1">'
#         txt += '<title>Password</title>'
#         txt += '</head>'
#         txt += '<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0" bgcolor="#ffffff" style="margin-top: 0;margin-bottom: 0;padding-top: 0;padding-bottom: 0;-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;-webkit-font-smoothing: antialiased;width: 100%;">'
#         txt += '<div class="navbar-brand" style="float: unset;padding: unset;height: unset;margin-left: 130px;margin-bottom: 43px"><h1 style="font-weight: 900"><span style="color: #1BBD36">3DIA</span>MOND</h1></div>'
#         txt +=  link
#         txt += '</body>'
#         txt += '</html>'

#         to = 'parshotam.kumar32@gmail.com'
#         subject = 'Your account successfully registered on 3diamond'
#         msg = EmailMultiAlternatives(subject, '', '', [to])
#         msg.attach_alternative(txt, "text/html")
#         msg.send()
#     except:
#         tb = sys.exc_info()[2]
#         tbinfo = traceback.format_tb(tb)[0]
#         msg = tbinfo + "\n" + str(sys.exc_type) + ": " + str(sys.exc_info())
        