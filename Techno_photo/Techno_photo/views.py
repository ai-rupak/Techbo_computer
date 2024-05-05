from django.shortcuts import render,redirect,HttpResponse
from techno.models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect

def BASE(request):

    return render(request,'base.html')

def INDEX(request):
    main_post = Post.objects.filter(section='Main_post' ,status=1).order_by('-id')
    popular_post = Post.objects.filter(section='Popular',status=1).order_by('-id')
    recent_post = Post.objects.filter(section='Recent',status=1)
    post = Post.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_no = request.POST.get('mobile_no')
        event_name = request.POST.get('event_name')
        date = request.POST.get('date')
        address = request.POST.get('address')
        message = request.POST.get('message')

        recipient = 'nandirakhi4@gmail.com'  # Set your recipient email address here
        sender = 'swarrupak@gmail.com'  # Set your sender email address here

        subject = f'New Inquiry: {event_name}'
        email_message = f'Name: {name}\nMobile Number: {mobile_no}\nEvent Name: {event_name}\nDate: {date}\nAddress: {address}\nMessage: {message}'
        send_mail(subject, email_message, sender, [recipient])
    

        client =Client(
            name = name,
            mobile_no = mobile_no,
            event_name = event_name,
            date = date,
            address = address,
            message = message,
        )
        # messages.success(request,Client.name + " successfully sent !")
        client.save()
        return redirect('index')

        


    context={
        'main_post':main_post,
        'popular_post':popular_post,
        'recent_post':recent_post,
        'post':post,


    }
    return render(request,'index.html',context)

def BLOG(request,id):
    recent_post = Post.objects.filter(section='Recent',status=1)
    post = Post.objects.filter(id=id)


    context={
        'recent_post':recent_post,
        'post':post,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_no = request.POST.get('mobile_no')
        event_name = request.POST.get('event_name')
        date = request.POST.get('date')
        address = request.POST.get('address')
        message = request.POST.get('message')

        recipient = 'pdrock5678@gmail.com'  # Set your recipient email address here
        sender = 'swarrupak@gmail.com'  # Set your sender email address here

        subject = f'New Inquiry: {event_name}'
        email_message = f'Name: {name}\nMobile Number: {mobile_no}\nEvent Name: {event_name}\nDate: {date}\nAddress: {address}\nMessage: {message}'
        send_mail(subject, email_message, sender, [recipient])
    

        client =Client(
            name = name,
            mobile_no = mobile_no,
            event_name = event_name,
            date = date,
            address = address,
            message = message,
        )
        # messages.success(request,Client.name + " successfully sent !")
        client.save()
        return redirect('index')
    

    return render(request, "blog.html",context)

def GALLERY(request):
    main_post = Post.objects.filter(section='Main_post' ,status=1).order_by('-id')
    popular_post = Post.objects.filter(section='Popular',status=1).order_by('-id')
    recent_post = Post.objects.filter(section='Recent',status=1)

    context={
        'main_post':main_post,
        'popular_post':popular_post,
        'recent_post':recent_post,



    }
    return render (request,"gallery.html",context) 

def VIDEO(request):
    return render (request,'video.html')



def my_view(request):
    # Redirect to the admin using the named URL pattern
    return HttpResponseRedirect(reverse("admin_site"))