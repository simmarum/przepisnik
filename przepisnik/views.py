from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import get_template
from rest_framework.decorators import api_view
from django.shortcuts import redirect

from .forms import ContactForm

from home.models import RateProduct
from home.models import Product
from django.db.models import Avg

from wagtail.core.models import Page


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
    if request.method == 'POST':
        product_id = request.POST.get('page_ptr_id')
        product_new_rate = request.POST.get('rate')
        try:
            product_id = int(product_id)
            product_new_rate = int(product_new_rate)
        except ValueError:
            return redirect(request.META['HTTP_REFERER'])

        new_rate_product = RateProduct(
            product_id=Page.objects.get(id=product_id),
            product_rate=product_new_rate
        )
        new_rate_product.save()
        new_avg_rate = RateProduct.objects.filter(
            product_id=product_id).aggregate(Avg('product_rate'))['product_rate__avg']
        updated_product = Product.objects.get(page_ptr_id=product_id)
        updated_product.difficult_level = new_avg_rate
        updated_product.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('/')
