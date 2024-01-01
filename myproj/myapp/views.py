from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(login)
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.is_valid()

        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        check = Register.objects.filter(email=email, password=password)
        if check:
            request.session['email'] = email
            return redirect(displayall)
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    return redirect(login)

def add(request):
    email = request.session.get('email')
    if email:
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect(add)
        form = BookForm()
        return render(request, 'add.html', {'form': form})
    return redirect(login)

def displayall(request):
    book = BookModel.objects.all()
    return render(request, 'displayall.html', {'book': book})

def display(request,id):
    email = request.session.get('email')
    if email:
        book = BookModel.objects.get(id=id)
        return render(request, 'display.html', {'book': book})
    return redirect(login)

def edit(request, id):
    book = BookModel.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        form.save()
        return redirect(displayall)
    else:
        form = BookForm(instance=book)
    return render(request, 'edit.html', {'form': form})

def delete(request, id):
    book = BookModel.objects.get(id=id)
    book.delete()
    return render(request, 'delete.html')

def logout(request):
    del request.session['email']
    return redirect(login)