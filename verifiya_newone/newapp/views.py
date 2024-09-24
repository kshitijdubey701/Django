from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Contact
from django.contrib import messages
from .models import LoginHistory
from django.contrib.auth.models import User
from .forms import InternshipForm
from .forms import ContactForm
# Create your views here.


# views.py

from django.shortcuts import render, redirect
from .forms import InternshipForm

def internship_application_view(request):
    if request.method == 'POST':
        # Include request.FILES to handle file uploads
        form = InternshipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after successful submission
    else:
        form = InternshipForm()

    return render(request, 'internship.html', {'form': form})


def home(request):
    return render(request, 'indexp.html')


def index(request):
    return render(request, 'indexp.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')



def team(request):
    return render(request, 'team.html')



# myapp/views.py



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Log the successful login in the history
            LoginHistory.objects.create(user=user, success=True)
            return redirect('home')  # Redirect to home page after successful login
        else:
            # If authentication fails, log the failed attempt
            user = User.objects.filter(username=username).first()
            if user:
                LoginHistory.objects.create(user=user, success=False)
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('home')  # Redirect to home page or success page after submission
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
    
