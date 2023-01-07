from django.shortcuts import render
from django.core.mail import send_mail
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == 'POST':
        #do stuff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['vanavara1986@gmail.com'], #to email
            fail_silently = False,
        )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        #return the page
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


# def about(request):
#     if request.method == 'POST':
#         #do stuff
#         message_name = request.POST['message-name']
#         message_email = request.POST['message-email']
#         message = request.POST['message']
#
#         send_mail(
#             message_name, #subject
#             message, #message
#             message_email, #from email
#             ['vanavara1986@gmail.com'], #to email
#             fail_silently = False,
#         )
#         return render(request, 'about.html', {'message_name': message_name})
#     else:
#         #return the page
#         return render(request, 'about.html', {})


def service(request):
    return render(request, 'service.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def blog_details(request):
    return render(request, 'blog_details.html', {})