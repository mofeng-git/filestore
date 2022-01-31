import datetime
from django.http import HttpResponse
from django.shortcuts import render

def sayHello(request):
  current_time = datetime.datetime.now()
  context1 = {}
  context1['centext'] = 'Hello World!'
  return render(request, 'index.html', context1)
       
def signUp(request): 
  return HttpResponse("还未开发完成。")

def signIn(request): 
  centext2 = {}
  centext2['apptitle'] = '简单云储存'
  return render(request, 'signIn.html', centext2)

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