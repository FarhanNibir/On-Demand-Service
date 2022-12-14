from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def home_view(request):
    return render(request, 'Home.html')


# def login_view(request):
#     return render(request, 'Login_Page.html')

@login_required
def signup_view(request):
    return render(request, 'signup.html')

@login_required
def driving_view(request):
    return render(request, 'driver.html')

@login_required
def aboutus(request):
    return render(request, 'About.html')

@login_required
def categorise(request):
    return render(request, 'categorise.html')

@login_required
def categorise_carwash(request):
    return render(request, 'carwash.html')

@login_required
def categorise_computer(request):
    return render(request, 'computer.html')

@login_required
def categorise_cleaning(request):
    return render(request, 'cleaning.html')

@login_required
def categorise_interior(request):
    return render(request, '')

@login_required
def categorise_homemaid(request):
    return HttpResponse('<h1 align="center">Home maid related work will appear here </h1>')


def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/home/')

    form = UserCreationForm()
    context={
        'register_form' : form,
    }
    return render(request, 'test.html',context)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')








