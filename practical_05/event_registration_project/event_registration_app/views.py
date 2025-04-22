from django.shortcuts import render, redirect, get_object_or_404
from .models import Registration
from .forms import RegistrationForm

def home(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    registrations = Registration.objects.all()
    return render(request, 'home.html', {'form': form, 'registrations': registrations})

def cancel_registration(request, id):
    Registration.objects.filter(id=id).delete()
    return redirect('home')