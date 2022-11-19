from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect
from .models import User_Detail
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    return render(request, 'patient_res/login.html', {'form': UserRegisterForm})
    # return HttpResponse("Hello, world. You're at the polls index.")
def register(request):
    return render(request, 'patient_res/register.html')

def userreg(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserRegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            username =form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            phno = form.cleaned_data['phone_no']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            userinst = User_Detail(user_name=username,password=password1,email=email,phone_no=phno,first_name=first_name,last_name=last_name)
            userinst.save()
            # name = form.cleaned_data['name']
            # number = form.cleaned_date['phone_number']
            # p = Person(name=name, phone_number=number, date_subscribed=datetime.now(), messages_recieved=0)
            # p.save(
            # redirect to a new URL:
            return HttpResponse('../register')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserRegisterForm()

    return render(request, 'patient_res/login.html', {'form': UserRegisterForm()})
