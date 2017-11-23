from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
]

# Added format suffixes to give URLs that explicitly refer to a given format - allows API to handle URLs such as http://example.com/api/items/4.json.
urlpatterns = format_suffix_patterns(urlpatterns)
