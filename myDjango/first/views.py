import datetime
from django.http import HttpResponse
 
def sayHello(request):
       s = 'Hello World!'
       current_time = datetime.datetime.now()
       html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
       return HttpResponse(html)
       
def signUp(request)
  pass

def signIn(request)
  pass

def loginOut(request)
  pass

def listFile(request)
  pass
  
def showPersonalinformation(request)
  pass

def uploadFile(request)
  pass

def downloadFile(request)
  pass