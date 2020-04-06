from django.shortcuts import render,HttpResponse
from newapp.models import Form
from django.contrib import messages
# Create your views here.

def form(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        phoneno=request.POST.get('phoneno')
        desc=request.POST.get('desc')
        form=Form(username=username,email=email,gender=gender,phoneno=phoneno,desc=desc)
        form.save()
        messages.success(request,'Data Has Been Stored!')
    return render(request,'form.html')