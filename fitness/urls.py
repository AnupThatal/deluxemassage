from django.urls import path,include
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",home,name='home'),
    path("about/",about,name='about'),
    path("service/",service,name='service'),
    path("blogs/",blogs,name='blogs'),
    path("therapist/",therapist,name='therapist'),
    path("course_purchase/<int:pk>/",course_purchase,name='course_purchase'),
    path("therapist_details/<int:id>/",therapist_details,name='therapist_details'),
    path("blog_details/<str:text>",blog_details,name='blog_details'),
    path("classes_details/<int:id>/",classes_details,name='classes_details'),
    path('add_cart/<int:pk>',add_cart,name='add_cart'),
    path('view_cart/',view_cart,name='view_cart'),    
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path("contact/<int:id>/",contact,name='contact'),
    path("course_purchase_cart/",course_purchase_cart,name='course_purchase_cart'),
    path("booked/",booked,name='booked')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)