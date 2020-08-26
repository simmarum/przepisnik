import urllib.parse

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

import ast

class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)

        context['products'] = Product.objects.child_of(self).live()

        return context


class Product(Page):
    sku = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=False)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_ingredients = models.TextField(blank=True, null=False)
    content_recipe = models.TextField(blank=True, null=False)
    content_additional = models.TextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('sku'),
        FieldPanel('category'),
        ImageChooserPanel('image'),
        FieldPanel('short_description'),
        FieldPanel('content_ingredients'),
        FieldPanel('content_recipe'),
        FieldPanel('content_additional'),
    ]

    def get_content_ingredients_as_list(self):
        return self.content_ingredients.split('\n')

    def get_content_additional_as_dict(self):
        """
        ..notes:
            [
                {
                    'name': 'timer',
                    'value': 10, # in seconds
                },
                {
                    'name': 'opis',
                    'value': 'Opis co się dzieje w danym kroku'
                },
            ]
        """
        available_things = [
            'timer',
            'opis'
        ]
        new_content_additional = []
        if self.content_additional != '':
            content_ingredients_py = ast.literal_eval(self.content_additional)
            for one_piece in content_ingredients_py:
                if one_piece['name'] in available_things:
                    new_content_additional.append(one_piece)
        return new_content_additional

    def get_context(self, request):
        context = super().get_context(request)
        context['relative_url'] = urllib.parse.urlparse(
            self.get_full_url()).path
        print(self.get_full_url())
        print(context['relative_url'])
        return context
