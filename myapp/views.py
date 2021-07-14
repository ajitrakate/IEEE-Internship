from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from myapp.models import Button, RequiredButton
from datetime import datetime

# Create your views here.

def HomePage(request):
    bulb = Button.objects.get(pk=1)
    bulbname = bulb.name
    bulbstate = "ON" if bulb.state else "OFF"
    connection = bulb.last_modification
    mydata = {'bulbname': bulbname, 'bulbstate': bulbstate, 'connection':connection}
    print(mydata)
    return render(request, 'myapp/home.html', mydata)

def change(request):
    bulb = RequiredButton.objects.get(pk=1)
    current_state = bulb.state
    bulb.last_modification = datetime.now()
    print(current_state)
    bulb.state = False if current_state else True
    bulb.save()
    return redirect('home')

def getData(request, k):
    bulb = RequiredButton.objects.get(pk=1)
    data = "ON" if bulb.state else "OFF"
    current_status = True if k==1 else False
    bulb = Button.objects.get(pk=1)
    bulb.state = current_status
    bulb.last_modification = datetime.now()
    bulb.save()
    mydata = {'bulb1':data}
    return JsonResponse(mydata)



    
