from .models import HomePage, Product
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
    )


@register(Product)
class ProductTR(TranslationOptions):
    fields = (
        'category',
        'short_description',
        'content_ingredients',
        'content_recipe',
        'content_additional'
    )
