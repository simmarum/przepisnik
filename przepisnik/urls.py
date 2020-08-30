from typing import Any, Dict, Optional

from django import template, urls
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

from . import views

app_name = 'przepisnik'

register = template.Library()

urlpatterns = [
    *i18n_patterns(url(r'^django-admin/', admin.site.urls)),

    *i18n_patterns(url(r'^admin/', include(wagtailadmin_urls))),
    *i18n_patterns(url(r'^documents/', include(wagtaildocs_urls))),

    *i18n_patterns(url(r'^search/$', search_views.search, name='search')),

    *i18n_patterns(url(r'^contact/', views.contact,  name='contact_us')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    *i18n_patterns(url(r"", include(wagtail_urls))),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r"^pages/", include(wagtail_urls)),
]


@register.simple_tag(takes_context=True)
def translate_url(context: Dict[str, Any], language: Optional[str]) -> str:
    """Get the absolute URL of the current page for the specified language.

    Usage:
        {% translate_url 'en' %}
    """
    url = context['request'].build_absolute_uri()
    return urls.translate_url(url, language)
