from django.shortcuts import render, redirect, get_object_or_404  
from .models import Registration  
from .forms import RegistrationForm  

def home(request):  
    registrations = Registration.objects.all()  
    return render(request, 'home.html', {'registrations': registrations})  

def register(request):  
    if request.method == "POST":  
        form = RegistrationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('home')  
    else:  
        form = RegistrationForm()  
    return render(request, 'register.html', {'form': form})  

def update_registration(request, id):  
    registration = get_object_or_404(Registration, id=id)  
    if request.method == "POST":  
        form = RegistrationForm(request.POST, instance=registration)  
        if form.is_valid():  
            form.save()  
            return redirect('home')  
    else:  
        form = RegistrationForm(instance=registration)  
    return render(request, 'register.html', {'form': form})  

def delete_registration(request, id):  
    Registration.objects.filter(id=id).delete()  
    return redirect('home')  