# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import UserRegistrationForm

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')  # Redirect to a login page or another page
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'users/register.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
#from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login as auth_login



# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('success_url')  # This should now work correctly
#     else:
#         form = UserRegistrationForm()
    
#     return render(request, 'users/register.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debugging line
            user = form.save()
            print("User saved to database:", user)  # Debugging line
            return redirect('success_url')
        else:
            print(form.errors)  # This will show form errors in the terminal
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})


def success_view(request):
    return render(request, 'users/success.html')  # Create a success.html template



def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)  # Log the user in
                # Redirect based on user role
                if user.role == 'fleet_manager':
                    return redirect('fleet_manager_home')  # Replace with your fleet manager page
                elif user.role == 'driver':
                    return redirect('driver_home')  # Replace with your driver page
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})



def fleet_manager_home_view(request):
    # Logic for the fleet manager's home page
    return render(request, 'users/fleet_manager_home.html')

def driver_home_view(request):
    # Logic for the driver's home page
    return render(request, 'users/driver_home.html')