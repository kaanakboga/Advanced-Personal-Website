from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from portfolio.models import Project, Skill, Service
from .models import CV

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()
    cv = CV.objects.first()
    form = ContactForm()

    return render(request, 'core/home.html', {
        'projects': projects,
        'skills': skills,
        'services': services,
        'cv': cv,
        'form': form,
    })

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            full_message = f"From: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

            send_mail(
                subject="New Contact Form Submission",
                message=full_message,
                from_email=email,
                recipient_list=['akbogakaan00@gmail.com'],
                fail_silently=False,
            )
            return redirect('home')
    return redirect('home')
