from django.shortcuts import render
from .forms import ContactForm

def index(request):
    context = {
            'title':'Home',
            'content': 'Welcome to Home',
    }
    return render(request,"index.html",context)

def about_page(request):
    context = {
            'title':'About Page',
            'content': 'Welcome to About Page',
    }
    return render(request,"index.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
            'title':'Contact Page',
            'content': 'Welcome to Contact Page',
            'form': contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request,"contact/view.html",context)

def login_page(request):
    form = LoginForm(request.POST or None)
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,"auth/login.html",{})

def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,"auth/register.html",{})
