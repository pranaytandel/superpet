"""
URL configuration for learndjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from demoapp import views
from django.views.generic.base import TemplateView,RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/",views.home,name="about"),
    path("",views.index,name="homepage"),
    path("contact/",views.contact,name="contact"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("comment/",RedirectView.as_view(url="/Details"),name="comment"),
    path("subjects/",views.subject,name="subject"),
    path("Details/",views.inputData,name="Details"),
    path("book/",views.Book.as_view(),name="book"),
    path("template-based-view",TemplateView.as_view(template_name="data.html",extra_context={"name":"pranay","age":18}),name="template"),
    path("pranay-based-view",TemplateView.as_view(template_name="pranay.html"),name="template"),

   
]
