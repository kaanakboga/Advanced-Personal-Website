from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from portfolio.models import Project, Skill, Service  # Doğru yerden çekiyoruz
from django.contrib.auth.models import User

try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'sifre123')
except:
    pass

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()
    form = ContactForm()

    return render(request, 'core/home.html', {
        'projects': projects,
        'skills': skills,
        'services': services,
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
