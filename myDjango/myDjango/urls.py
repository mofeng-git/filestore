"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first import views
urlpatterns = [
  path('', views.sayHello),
#    path('admin/', admin.site.urls),
  path(r'signUp',views.signUp),
  path(r'signIn',views.signIn),
  path(r'loginOut',views.loginOut),
  path(r'listFile',views.listFile),
  path(r'showPersonalinformation',views.showPersonalinformation),
  path(r'uploadFile',views.uploadFile),
  path(r'downloadFile',views.downloadFile),
]
