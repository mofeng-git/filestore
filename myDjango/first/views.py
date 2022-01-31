import datetime
from django.http import HttpResponse
from django.shortcuts import render

def sayHello(request):
  current_time = datetime.datetime.now()
  context          = {}
  context['centext'] = 'Hello World!'
  return render(request, 'index.html', context)
       
def signUp(request): 
  return HttpResponse("还未开发完成。")

def signIn(request): 
  return HttpResponse("还未开发完成。")
  pass

def loginOut(request): 
  return HttpResponse("还未开发完成。")
  pass

def listFile(request): 
  return HttpResponse("还未开发完成。")
  pass
  
def showPersonalinformation(request): 
  return HttpResponse("还未开发完成。")
  pass

def uploadFile(request): 
  return HttpResponse("还未开发完成。")
  pass

def downloadFile(request): 
  return HttpResponse("还未开发完成。")
  pass