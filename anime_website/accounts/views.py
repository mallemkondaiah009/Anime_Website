from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Adjust the redirect as needed
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/sign up.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    """
    Handles user login. 
    Renders the login form and authenticates the user upon submission.
    """
    if request.method == 'POST':
        # Get username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login the user and redirect to home page or dashboard
            login(request, user)
            return redirect('home')  # You can change 'home' to any URL name you want
            
        else:
            # Authentication failed
            messages.error(request, "Invalid username or password")
            return redirect('login')  # Redirect back to the login page

    # GET request - Render the login page
    return render(request, 'accounts/login.html')

