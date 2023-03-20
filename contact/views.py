from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def contactus(request):
    if request.method == 'POST':
        # form = ContactForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        content = request.POST['content']

        html = render_to_string('contact/email.html',{
            'name':name,
            'email':email,
            'subject':subject,
            'content':content
        })

        send_mail(subject=subject,message=content,recipient_list=['v0243614@gmail.com'],from_email=email,html_message=html)
        messages.success(request, 'Your Query is submtted,')
        messages.success(request, 'We will contact you soon.')
        return redirect('contactus')

    return render(request, "contact/contact-us.html")