import urllib.parse

from django.db import models

from django.core.paginator import Paginator

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search.models import Query
from wagtail.search import index

import ast


class HomePage(Page):
    def get_context(self, request):
        PAGINATION_NUM = 6
        context = super().get_context(request)

        categories = Product.objects.child_of(
            self).live().values('category').distinct().order_by("category")
        context['categories'] = [cat['category'] for cat in categories]
        get_req = "?"
        search_query = request.GET.get('query', None)
        if search_query == "":
            search_query = None
        if search_query:
            get_req += f"query={search_query}"
            search_results = Product.objects.child_of(self).live().search(
                search_query,
                fields=["title", "category"]
            )
            # Log the query so Wagtail can suggest promoted results
            Query.get(search_query).add_hit()
        else:
            search_results = Product.objects.child_of(
                self).live().select_related('image')
        print("@@@", "typeof search_query", type(search_results))

        paginator = Paginator(search_results, PAGINATION_NUM)
        page_number = int(request.GET.get('page', 1))
        page_obj = paginator.get_page(page_number)

        con = "&"
        if "?query=" not in get_req:
            con = ""
        if page_obj.has_next():
            context['products_next_page'] = get_req + \
                f"{con}page={page_number+1}"
        if page_obj.has_previous():
            context['products_has_previous'] = get_req + \
                f"{con}page={page_number-1}"

        context['products'] = page_obj

        return context


class Product(Page):
    category = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=False)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    difficult_level = models.FloatField(blank=False, null=False)
    content_ingredients = models.TextField(blank=True, null=False)
    content_recipe = models.TextField(blank=True, null=False)
    content_additional = models.TextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('category'),
        FieldPanel('difficult_level'),
        ImageChooserPanel('image'),
        FieldPanel('short_description'),
        FieldPanel('content_ingredients'),
        FieldPanel('content_recipe'),
        FieldPanel('content_additional'),
    ]

    search_fields = [
        index.SearchField('title'),
        index.SearchField('category'),
        index.FilterField('path'),
        index.FilterField('depth'),
        index.FilterField('live')
    ]

    def get_content_ingredients_as_list(self):
        return self.content_ingredients.split('\n')

    def get_content_star_rating(self):
        star_rating = [0]*5
        for number in range(round(self.difficult_level)):
            star_rating[number] = 1
        return star_rating

    def get_content_additional_as_dict(self):
        """
        ..notes:
            [
                {
                    'name': 'timer',
                    'value': 10, # in seconds
                },
                {
                    'name': 'description',
                    'value': 'Opis co się dzieje w danym kroku'
                },
            ]
        """
        available_things = [
            'timer',
            'description'
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
        context['my_relative_url'] = urllib.parse.urlparse(
            self.get_full_url()).path
        return context


class RateProduct(models.Model):
    product_id = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.PROTECT,
        related_name='+'
    )
    product_rate = models.IntegerField(
        null=False,
        blank=False
    )
