from django.conf.urls import url

from . import views


urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    url(r'^county_div1/$', views.county_div1, name='county_div1'),
    url(r'^county_div2/$', views.county_div2, name='county_div2'),
    url(r'^eng_test/$', views.eng_test, name='eng_test'),
    url(r'^eng_odi/$', views.eng_odi, name='eng_odi'),
]
