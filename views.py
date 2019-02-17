from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404
from .models import Question,Choice,Users,Locations,Events,Join
from django.urls import reverse

from django.views import generic
import pdb
import logging

def join_activity(request):
    d=request.POST
    u_id=d['user_id']
    e_id=d['event_id']
    user=Users.objects.get(user_id=u_id)
    event=Events.objects.get(pk=e_id)
    join=Join.objects.filter(user_id=u_id,event_id=e_id)
    if len(join)==0:
        join=Join(user=user,event=event,is_inviter=False)
        join.save()
        return render(request,"polls/show_error_message.html",{"error":"成功参加。","user":user})
    else:
        return render(request,"polls/show_error_message.html",{"error":"不能重复参加活动。","user":user})

def show_my_activities(request):
    d=request.POST
    if 'button' in d:
        flag=d['flag']
        k=d['button']
        user=Users.objects.get(pk=k)
        cnt_event=[]
        join=Join.objects.filter(user_id=k)
        event_list=[]
        for j in join:
            event_list+=Events.objects.filter(id=j.event_id)
        for e in event_list:
            cnt_event.append(Join.objects.filter(event_id=e.id).__len__())
        return render(request, "polls/showMine.html", {'user':user, 'event_list':event_list, 'cnt_event':cnt_event})


def show_activities(request):
    d=request.POST
    if 'button' in d:
        k=d['button']
        user=Users.objects.get(pk=k)
        event_list=Events.objects.all()
        cnt_event=[]
        for e in event_list:
            cnt_event.append(Join.objects.filter(event_id=e.id).__len__())

        return render(request,"polls/ground.html",{'user':user,'event_list':event_list,'cnt_event':cnt_event})
        # else:
        #     join=Join.objects.filter(user_id=k)
        #     event_list=[]
        #     for j in join:
        #         event_list+=Events.objects.filter(id=j.event_id)
        #     return render(request, "polls/showMine.html", {'user':user, 'event_list':event_list, 'cnt_event':cnt_event, 'num':num})

def showinfo(request):
    if 'button' in request.POST:
        k=request.POST['button']
        user=Users.objects.get(pk=k)
    return render(request,"polls/personal_message.html",{'user':user})


def submit_activity(request):
    if 'button' in request.GET:
        k=request.GET['button']
        user=Users.objects.get(pk=k)
        location_list=Locations.objects.all()
        return render(request,"polls/submit_activity.html",{'user':user,"location_list":location_list})
    if 'button' in request.POST:
        d=request.POST;
        user=Users.objects.get(pk=d['button'])
        user.phone_number=d['phone_number']
        user.save()
        loc=Locations.objects.get(location_name=d['selected_location'])
        event=Events(start_time=d['begin_time'],end_time=d['end_time'],\
                     location=loc,event_text=d['event_detail'],event_title=d['title'])
        event.save()
        jo=Join(event_id=event.id,user_id=user.user_id,is_inviter=True)
        jo.save()
        return render(request,'polls/home_page.html',{'user':user})


def profile(request):
    if len(request.POST)<2:
        error="Please Sign in First"
        return render(request,"polls/Signin.html",context={"error_message":error})

    email=request.POST['email']
    password=request.POST['password']
    exist=False
    for t in Users.objects.values("email"):
        if t["email"] == email:
            exist=True
            break
    location_list=Locations.objects.all()
    if exist:
        user = Users.objects.filter(email=email)[0]
        if password == user.password:
            return render(request, "polls/home_page.html", context={"user":user, "location_list":location_list})
        else:
            return render(request,"polls/Signin.html",context={"error_message" : "password error!"})
    u=Users()
    u.email=email
    u.user_id=email
    u.name=email[:email.find('@')]
    u.password=password
    u.save()
    # # pdb.set_trace()
    return render(request, "polls/home_page.html", context={"user":u, "location_list":location_list})


def login(request):
    # # pdb.set_trace()
    return render(request,'polls/Signin.html',{})


def detail(request):
    if 'choice' in request.POST:
        question = get_object_or_404(Question,pk=request.POST['choice'])
        question.votes += 1;
        question.save();
        questions=Question.objects.all()
        return render(request, 'polls/detail.html', {'questions': questions})
    else:
        return render(request, 'polls/detail.html', {
            'error_message': "You didn't select a choice.",
        })


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'


def results(request,pk):
    result_alone=Question.objects.get(pk=pk);
    # result_alone.choice_set
    # # pdb.set_trace()#use result_alone.chocie
    return render(request,'polls/results.html',{'result_alone':result_alone})


def index(request):
    return render(request,"polls/Signin.html",{})
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    if len(context)==0:
        context['error']="NO objects"
    return render(request,'polls/index.html',context)