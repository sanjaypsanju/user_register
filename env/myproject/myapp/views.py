from django.shortcuts import render,HttpResponse,redirect
from.forms import LoginForm,RegisterForm
from django.contrib import messages  # Import messages module for displaying messages

from.models import Login,Register
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form['username'].valid()
            password = form['password'].valid()
            try:
                user = Login.objects.get(username=username, password=password)
                if user is not None:
                    return render(request, 'home.html')
            except:
                pass
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        uname = request.POST.get('name')
        mail = request.POST.get('mail')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password == confirmpassword:
            try:
                # Create the user object without specifying 'name' (use first_name and last_name fields instead)
                my_user = User.objects.create_user(username=username, email=mail, password=password)
                my_user.first_name = uname  # Set first_name as 'uname'
                my_user.save()
                print(my_user)
                return redirect('login')  # Redirect to login page upon successful user creation
            except Exception as e:
                return HttpResponse("Error creating user: " + str(e))
        else:
            return HttpResponse("Passwords do not match.")
    else:
        return render(request, 'register.html')
