import datetime
from django.http import HttpResponse
 
def sayHello(request):
  current_time = datetime.datetime.now()
  context          = {}
  context['centext'] = 'Hello World!' + current_time
    return render(request, 'index.html', context)
  return HttpResponse(html)
       
def signUp(request): 
  return HttpResponse("还未开发完成。")

def signIn(request): 
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