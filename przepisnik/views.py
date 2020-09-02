from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import get_template
from rest_framework.decorators import api_view
from django.shortcuts import redirect

from .forms import ContactForm


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name', '')
            contact_email = request.POST.get(
                'contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return render(request, 'contact.html', {
                'form': form_class,
            })

    return render(request, 'contact.html', {
        'form': form_class,
    })


def rate_product(request):
    print("!", request)
    return redirect('/')
