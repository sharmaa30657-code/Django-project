from django.shortcuts import render, redirect, get_object_or_404
from .models import Memeber
from .forms import MemeberForm

def home(request):
    members = Memeber.objects.all()
    return render(request, 'myapp/home.html', {'members': members})

def contact(request):
    return render(request, "myapp/contact.html")

def about(request):
    return render(request, "myapp/about.html")

def update_member(request, id):
    member = Memeber.objects.get(id=id)

    if request.method == "POST":
        form = MemeberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemeberForm(instance=member)

    return render(request, 'myapp/update.html', {'form': form})


def delete_member(request, id):
    member = get_object_or_404(Memeber, id=id)

    if request.method == 'POST':
        member.delete()
        return redirect('home')

    return render(request, 'myapp/delete.html', {'member': member})

def add_member(request):
    if request.method == "POST":
        form = MemeberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemeberForm()

    return render(request, 'myapp/add.html', {'form': form})