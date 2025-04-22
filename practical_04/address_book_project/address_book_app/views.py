from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'form': form, 'contacts': contacts})

def update_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'update.html', {'form': form})

def delete_contact(request, id):
    Contact.objects.filter(id=id).delete()
    return redirect('home')