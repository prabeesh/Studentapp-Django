from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from studentapp.models import student

def mainpage(request):
  if request.method == 'GET':
    c = {}
    c.update(csrf(request))
    return render_to_response("mainpage.html", c)


def details(request):
  if request.method == 'GET':
    c = {}
    c.update(csrf(request))
    return render_to_response("test.html", c)
	

  if request.method == 'POST':
    name =request.POST.get('student_name')
    sex =request.POST.get('sex')
    age =request.POST.get('age')
    mark =request.POST.get('mark')
    p = student(name = name, sex = sex, age= age, mark= mark)
    p.save()
    return HttpResponse('saved')
	

def sort1(request):
  entries = student.objects.order_by('age')
  t = get_template('show_entries.html')
  html=t.render(Context({'entries':entries})) 
  return HttpResponse(html)

def sort2(request):
  entries = student.objects.order_by('-mark')
  t = get_template('show_entries.html')
  html=t.render(Context({'entries':entries}))
  return HttpResponse(html)

def remove(request):
  if request.method == 'GET':
    d = {}
    d.update(csrf(request))
    return render_to_response("input.html", d)

  if request.method=='POST':
    name =request.POST.get('student_name')
    p=student.objects.filter(name=name)
    p.delete()
    return HttpResponse("remove")

def search(request):
  if request.method == 'GET':
    e = {}
    e.update(csrf(request))
    return render_to_response("input.html", e)

  if request.method=='POST':
    name =request.POST.get('student_name')
    entries=student.objects.filter(name=name)
    t = get_template('show_entries.html')
    html=t.render(Context({'entries':entries}))
    return HttpResponse(html)
