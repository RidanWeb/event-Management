from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  
from users.forms import UserCreationForm, customRegistrationForm


# Create your views here.

def sign_up(request):
    
    # if request.method == 'GET':
    # form = UserCreationForm()
    form = customRegistrationForm()
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = customRegistrationForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            
            #registration successfull message
            messages.success(request, 'Registration successful. You can now log in.')
            
            
            
            
            
            
            
            return redirect('sign_in')  # Redirect to the sign-in page after successful registration
            # username = form.cleanned_data['username']
            # password = form.cleaned_data['password1']
            # confirm_password = form.cleaned_data['password2']
        #     username = form.cleaned_data.get('username')
        #     password = form.cleaned_data.get('password1')
        #     confirm_password = form.cleaned_data.get('password2')
        #     if password == confirm_password:
        #         User.objects.create_user(username=username, password=password)
                
        #     else:
        #         # Handle the case where passwords do not match
        #         form.add_error('password2', 'Passwords do not match.')
        # else:
        #     # Handle the case where the form is not valid
        #     print(f"{form.errors} Form is not valid.")  # Print form errors to the console for debugging
            
            
    return render(request, 'registered/signup.html', {'form': form})






def signin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # print(f"Username: {username}, Password: {password}")  # Debugging line
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to a success page.
        
    
    return render(request, 'registered/signin.html')


def sign_out(request):
    if request.method == 'POST':
        logout(request)
        # return redirect('sign_in')
        return redirect('home')
    return redirect('home')
    
