from django.conf.urls import url
from . import views, models

app_name = 'books'
urlpatterns = [   
    url(r'^$', views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^meta/$', views.display_meta),
    # url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search, {'model': models.Book}),
    url(r'^contact/$', views.contact),
]