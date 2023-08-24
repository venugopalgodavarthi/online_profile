from django.shortcuts import render, redirect
from django.http import HttpResponse
from userprofile.forms import UserProfile_form
from userprofile.models import UserProfile_model
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# Create your views here.


def register_profile(request):
    if request.method == 'POST':
        form = UserProfile_form(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            subject = 'welcome to Online PROFILE World'
            message = f'Hi {user.name}, Thank you for Given your Details in Online Profile World.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            send_mail(subject, message, email_from, recipient_list)
            print(user.name, user.id, user.email)
            subject = 'We got New Profile Details'
            message = f'''Name:{user.name}\nEmail:{user.email}\nPhone:{user.phone}\nDesc:{user.desc}\npic:{user.profile_picture.url}\n 
            Thank you.'''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['gvg.9966@gmail.com',]
            email = EmailMessage(subject, message, email_from, recipient_list, attachments=[
                ('user.profile_picture.url', 'user.profile_resume.url')])
            email.send(fail_silently=False)
            return redirect(f'/user/display/{user.id}/')
    else:
        form = UserProfile_form()
    return render(request, 'home.html', {'form': form})


def display_profile(request, pk):
    if request.method == 'GET':
        user = UserProfile_model.objects.get(id=pk)
        return render(request, 'details.html', {'user': user})


def update_profile(request, pk):
    if request.method == 'POST':
        res = UserProfile_model.objects.get(id=pk)
        form = UserProfile_form(request.POST, request.FILES, instance=res)
        if form.is_valid():
            user = form.save()
            subject = 'welcome to Online PROFILE World'
            message = f'Hi {user.name}, Thank you for registering in Online Profile World.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            send_mail(subject, message, email_from, recipient_list)
            return redirect(f'/user/display/{user.id}/')
    else:
        res = UserProfile_model.objects.get(id=pk)
        form = UserProfile_form(instance=res)
    return render(request, 'home.html', {'form': form})


def details_profile(request):
    user = UserProfile_model.objects.all()
    return render(request, 'display._details.html', {'form': user})


def delete_profile(request, pk):
    if request.method == 'POST':
        UserProfile_model.objects.get(id=pk).delete()
        return redirect('/user/details/')
    else:
        form = UserProfile_model.objects.get(id=pk)
    return render(request, 'delete_confirm.html', {'form': form})
