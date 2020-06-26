from django.shortcuts import render
from teacher.models import categories, Courses, VideoUploads, Sections, questions
from home.models import User, user_profile
from datetime import datetime
import os, sys, shutil
import traceback
from django.http import HttpResponse, HttpResponseRedirect
import json
import uuid
from django.conf import settings


def teacher_account(request):
    objC = categories.objects.all()
    profile = user_profile.objects.get(user_id=request.user.id)
    return render(request, 'teacher/account.html', {'objC':objC, 'profile':profile})

def teacher_security(request):
    return render(request, 'teacher/security.html', {})

def teacher_notifications(request):
    return render(request, 'teacher/notifications.html', {})
    
def teacher_payments(request):
    return render(request, 'teacher/payments.html', {})

def teacher_privacy(request):
    return render(request, 'teacher/privacy.html', {})

def dashboard(request):
    return render(request, 'teacher/dashboard.html', {}) 

def teacher_courses(request):
    course_list = getAllCourseList()
    return render(request, 'teacher/courses.html', {'course_list': course_list}) 

def teacher_faqs(request):
    return render(request, 'teacher/faqs.html', {}) 

def course_engagement(request):
    return render(request, 'teacher/course-engagement.html', {})  

def student_performance(request):
    return render(request, 'teacher/student-performance.html', {})  
    
def teacher_messages(request):
    return render(request, 'teacher/messages.html', {'datetime':datetime})  
      

def dashboard1(request):
    return render(request, 'teacher/dashboard_1.html', {})    

def guideline(request):
    return render(request, 'teacher/guidline.html', {})    
    
def teacher_help(request):
    return render(request, 'teacher/help.html', {})    

def help2(request):
    return render(request, 'teacher/help2.html', {})    

def newcourse2(request):
    return render(request, 'teacher/new-course-2.html', {})    

def newcourse3(request):
    return render(request, 'teacher/new-course-3.html', {})    

def newcourse4(request):
    id = request.GET.get('id')
    data = get_courseDetails(id)
    return render(request, 'teacher/new-course-4.html', {'video_list': data['video_list'], 'question_list': data['question_list'], 'section_list': data['section_list']})    

def newcourse5(request):
    return render(request, 'teacher/new-course-5.html', {})    

def newcourse(request):
    obj_cat = categories.objects.all()
    return render(request, 'teacher/new-course.html', {'categories':obj_cat})    

def nocourseengagement(request):
    return render(request, 'teacher/no-course-engagement.html', {})    

def nocourse(request):
    return render(request, 'teacher/no-course.html', {})

# post

# get all course list
# @return List
def getAllCourseList():
    course_list = []
    course_list = Courses.objects.all()
    return course_list

# store course in DB
def store_course(request):
    received_json_data = json.loads(request.body)
    data = received_json_data['data']    
    msg = ''
    id = ''
    try:
        print("data", data)
        name = data['name']        
        description = data['description']
        requirements = data['requirements']
        gains = data['gains']
        todo = data['todo']
        category_id = data['category_id']
        sub_category_id = data['sub_category_id']
        price = data['price']
        tags = data['tags']

        objCourse = Courses(
            name = name,
            description = description,
            requirements = requirements,
            gains = gains,
            includes = todo,
            scat_id = sub_category_id,
            price = price,
            tags = tags,
            user_id=request.user.id,
        )
        objCourse.save()
        print('success')
        msg = "successs"
        id = objCourse.id
        print("--successfully created , id", objCourse.id)
    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n" +  ": " + str(sys.exc_info())
    #
    to_return = {
        'msg': msg,
        'id': id}
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")

# store videos in DB
def store_course_2(request):
    data = request.POST
    course_id = json.loads(data.get("course_id"))
    files = request.FILES
    video_list = []
    print(files)
    msg = ''
    try:
        section_list = data.get("section_list")
        section_list = json.loads(section_list)
        json_video_list = json.loads(data.get("video_list"))      

        if( len(json_video_list) > 0 ):
            ## store section in DB
            for section in section_list:
                name = section['name']
                tag_id = section['tag_id']

                ## store section in DB
                objSection = Sections(
                    name=name,
                    course_id=course_id,
                    type='video',
                )
                objSection.save()
                section_id = objSection.id
                for item in json_video_list:
                    if( item['sectionId'] == tag_id ) :

                        ## upload video
                        video_key = item['key']
                        video = files[video_key]
                        
                        filename = video._get_name()
                        ext = filename[filename.rfind('.'):]
                        file_name = str(uuid.uuid4())+ext
                        path = '/uploads/courses/videos/'
                        full_path= str(path) + str(file_name)
                        fd = open('%s/%s' % (settings.STATICFILES_DIRS[0],str(path) + str(file_name)), 'wb')      
                        for chunk in video.chunks():
                            fd.write(chunk)
                        fd.close()

                        ## store video in DB
                        objVideo = VideoUploads(
                            name=filename,
                            section_id=section_id,
                            url=full_path,
                        )
                        objVideo.save()
            msg = "success"
        else:
            msg = "failed"
    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n" +  ": " + str(sys.exc_info())
    to_return = {
        'msg': msg,
    }
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")

# store questions in DB
def store_course_3(request):
    msg = ''
    data = request.POST
    course_id = json.loads(data.get("course_id"))
    try:
        question_list = json.loads(data.get('question_list'))
        section_list = json.loads(data.get('section_list'))
        print("question list", question_list)
        print("section list", section_list)
        if( len(question_list) > 0 ) :
            for section in section_list:
                tag_id = section['tag_id']
                section_name = section['name']

                ## store section in DB
                objSection = Sections(
                    name=section_name,
                    course_id=course_id,
                    type='question',
                )
                objSection.save()
                section_id = objSection.id

                for question in question_list:
                    if question['section_id'] == tag_id :
                        title = question['question_title']
                        type = question['answer_type']
                        answers = question['answers']

                        aw_1_type = answers[0]['type']
                        aw_1_result = answers[0]['result']
                        aw_1_data = answers[0]['data']

                        aw_2_type = answers[1]['type']
                        aw_2_result = answers[1]['result']
                        aw_2_data = answers[1]['data']

                        aw_3_type = answers[2]['type']
                        aw_3_result = answers[2]['result']
                        aw_3_data = answers[2]['data']

                        aw_4_type = answers[3]['type']
                        aw_4_result = answers[3]['result']
                        aw_4_data = answers[3]['data']

                        objQuestion = questions(
                            title=title,
                            type=type,
                            section_id=section_id,
                            aw_1_type=aw_1_type,
                            aw_1_result=aw_1_result,
                            aw_1_data=aw_1_data,

                            aw_2_type=aw_2_type,
                            aw_2_result=aw_2_result,
                            aw_2_data=aw_2_data,

                            aw_3_type=aw_3_type,
                            aw_3_result=aw_3_result,
                            aw_3_data=aw_3_data,

                            aw_4_type=aw_4_type,
                            aw_4_result=aw_4_result,
                            aw_4_data=aw_4_data,
                        )
                        objQuestion.save()

            msg = "success"
        else :
            msg = "failed"
    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        msg = tbinfo + "\n" +  ": " + str(sys.exc_info())
    to_return = {
        'msg': msg,
    }
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")

# get course details by course's id.
#
# @param Request
#
# @return HttpResponse
def getCourseDetailsById(request):
    id = request.POST.get('id')
    msg = ''
    to_return = {
        'msg': msg,
        'data': get_courseDetails(id)
    }
    serialized = json.dumps(to_return)
    return HttpResponse(serialized, content_type="application/json")

def get_courseDetails(course_id):
    id = course_id
    video_list = []
    question_list = []
    section_list = []
    tmp_sections = Sections.objects.filter(course_id=id)

    if len(tmp_sections) > 0:
        for section in tmp_sections:
            section_list.append({
                'id': section.id,
                'name': section.name,
                'course_id': section.course_id,
                'type': section.type,
            })
            for video in VideoUploads.objects.filter(section_id=section.id):
                video_list.append({
                    'id': video.id,
                    'name': video.name,
                    'section_id': video.section_id,
                    'src': video.url,
                })
            for question in questions.objects.filter(section_id=section.id):
                question_list.append({
                    'id': question.id,
                    'title': question.title,
                    'type': question.type,
                    'section_id': question.section_id,
                    'aw_1_type': question.aw_1_type,
                    'aw_1_result': question.aw_1_result,
                    'aw_1_data': question.aw_1_data,
                    'aw_2_type': question.aw_2_type,
                    'aw_2_result': question.aw_2_result,
                    'aw_2_data': question.aw_2_data,
                    'aw_3_type': question.aw_3_type,
                    'aw_3_result': question.aw_3_result,
                    'aw_3_data': question.aw_3_data,
                    'aw_4_type': question.aw_4_type,
                    'aw_4_result': question.aw_4_result,
                    'aw_4_data': question.aw_4_data,
                })
    print(section_list)
    return {
        'question_list': question_list,
        'video_list': video_list,
        'section_list': section_list,
    }