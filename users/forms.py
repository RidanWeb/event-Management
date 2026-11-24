from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User  

from events.form import StyledFormMixin

class UserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  
        
          
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for field_name, field in self.fields.items():
            self.fields[field_name].help_text = None  # Remove help text
            
            
            
            


class customRegistrationForm(StyledFormMixin, forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'confirm_password']
        
        
    def clean_email(self):
        
        email = self.cleaned_data.get('email')
        
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email
    
    def clean_username(self):
        
        username = self.cleaned_data.get('username')
        
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username
    
    
       
    def clean_password1(self):
        
        password1 = self.cleaned_data.get('password1')
        errors = []
        # confirm_password = self.cleaned_data.get('confirm_password')
        # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
        # confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
        
        
        
        if len(password1) < 8:
            errors.append("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in password1):
            errors.append("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password1):
            errors.append("Password must contain at least one lowercase letter.")
        if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in password1):
            errors.append("Password must contain at least one special character.")
        if not any(char.isdigit() for char in password1):
            errors.append("Password must contain at least one digit.")
        if not any(char.isalpha() for char in password1):
            errors.append("Password must contain at least one letter.")  
            
        if errors:
            raise forms.ValidationError(errors)
        
        return password1
    
    
    
    # non field errors
    def clean(self):
        
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("confirm_password")

        if password1 and confirm_password and password1 != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
            
        return cleaned_data  
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user  
        